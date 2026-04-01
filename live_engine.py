"""Background live engine that updates shared state continuously."""
import time
import random
import asyncio
from typing import Any

from generator import generate_account, generate_transaction
from live_state import accounts, alerts, transactions
from ws_manager import manager


def run_live_engine(pamrs_engine: Any, graph_engine: Any, nlp_engine: Any, delay: float = 1.0) -> None:
    """
    Seed accounts and continuously emit accounts/transactions.

    Args:
        pamrs_engine: PAMRSEngine instance
        graph_engine: GraphEngine instance
        nlp_engine: NLPDetector instance
        delay: seconds between loops
    """
    if not accounts:
        for _ in range(10):
            acc = generate_account()
            score = pamrs_engine.calculate_pamrs(acc)
            acc["pamrs_score"] = score
            acc["risk_flag"] = pamrs_engine.risk_label(score)
            accounts.append(acc)

    while True:
        # Occasionally add a new account
        if random.random() < 0.3:
            acc = generate_account()
            score = pamrs_engine.calculate_pamrs(acc)
            acc["pamrs_score"] = score
            acc["risk_flag"] = pamrs_engine.risk_label(score)
            accounts.append(acc)

            if score > 70:
                alerts.append({
                    "type": "ACCOUNT_RISK",
                    "account_id": acc["account_id"],
                    "score": score,
                })

        # Generate and process a transaction
        if len(accounts) > 2:
            tx = generate_transaction(accounts)
            transactions.append(tx)

            graph_engine.add_transaction(
                tx["sender"],
                tx["receiver"],
                tx["amount"],
                tx["device_id"],
            )

            # NLP similarity on recent remarks
            remark_window = [t.get("remark", "") for t in list(transactions)[-50:]]
            suspicious = nlp_engine.detect_similar_transactions(remark_window)

            if suspicious:
                alerts.append({
                    "type": "NLP_PATTERN",
                    "message": "Similar remarks detected",
                    "count": len(suspicious),
                })

            if tx["amount"] >= 900000:
                alerts.append({
                    "type": "STRUCTURING",
                    "amount": tx["amount"],
                    "device_id": tx["device_id"],
                })

        # Push live snapshot to WebSocket clients (non-blocking)
        try:
            manager.enqueue_broadcast({
                "type": "UPDATE",
                "accounts": accounts[-50:],
                "transactions": list(transactions)[-50:],
                "alerts": list(alerts)[-10:],
            })
        except Exception:
            pass

        time.sleep(delay)
