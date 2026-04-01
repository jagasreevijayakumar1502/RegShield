"""Lightweight live stream wrapper for generating/streaming synthetic fraud activity."""
import time
import threading
from typing import Callable, Dict, Any, List, Optional

from data_generator import generate_account, generate_transaction, generate_mule_cluster

# Mutable store used by the streamer thread
accounts: List[Dict[str, Any]] = []


def start_stream(
    process_account: Callable[[Dict[str, Any]], None],
    process_transaction: Callable[[Dict[str, Any]], None],
    delay: float = 1.0,
    stop_event: Optional[threading.Event] = None,
) -> None:
    """
    Start the real-time stream: seed accounts, inject mule cluster, then emit transactions forever.

    Args:
        process_account: callback for every new account created.
        process_transaction: callback for every transaction emitted.
        delay: seconds to wait between transactions.
        stop_event: optional threading.Event to allow graceful shutdown.
    """
    accounts.clear()

    # Seed normal accounts
    for _ in range(10):
        acc = generate_account()
        accounts.append(acc)
        process_account(acc)

    # Inject a mule cluster using a shared device
    fraud_accounts = generate_mule_cluster(accounts)
    for acc in fraud_accounts:
        process_account(acc)

    # Continuous transaction feed
    while True:
        if stop_event and stop_event.is_set():
            break

        tx = generate_transaction(accounts)
        process_transaction(tx)
        time.sleep(delay)
