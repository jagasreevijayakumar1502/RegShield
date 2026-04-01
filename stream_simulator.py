"""
Real-Time Transaction Stream Simulator
Simulates live transaction processing for fraud detection demonstration.
"""
import time
import random
from typing import List, Dict, Any, Callable
from datetime import datetime, timedelta


class StreamSimulator:
    """
    Real-time transaction streaming simulator for fraud detection demos.

    Streams transactions with configurable delays to simulate live processing.
    """

    def __init__(self, processor_func: Callable[[Dict[str, Any]], None]):
        """
        Initialize stream simulator.

        Args:
            processor_func: Function to process each transaction
        """
        self.processor = processor_func
        self.is_streaming = False
        self.processed_count = 0
        self.alerts_triggered = 0

    def stream(self, transactions: List[Dict[str, Any]], delay: float = 0.5,
               batch_size: int = 1, show_progress: bool = True) -> Dict[str, Any]:
        """
        Stream transactions with real-time processing.

        Args:
            transactions: List of transaction dictionaries
            delay: Delay between transactions (seconds)
            batch_size: Process multiple transactions at once
            show_progress: Show processing progress

        Returns:
            Processing statistics
        """
        self.is_streaming = True
        self.processed_count = 0
        self.alerts_triggered = 0

        start_time = time.time()

        print("🚀 Starting Real-Time Transaction Stream")
        print(f"📊 Processing {len(transactions)} transactions...")
        print("=" * 60)

        try:
            for i in range(0, len(transactions), batch_size):
                batch = transactions[i:i + batch_size]

                for tx in batch:
                    if show_progress:
                        tx_id = tx.get('Transaction_ID') or tx.get('transaction_id') or f"TX-{i+1}"
                        print(f"⚡ Processing {tx_id}: {tx.get('sender', 'Unknown')} → {tx.get('receiver', 'Unknown')} | ₹{tx.get('amount', 0)}")

                    # Process transaction
                    self.processor(tx)
                    self.processed_count += 1

                    # Add random delay to simulate real-time processing
                    if delay > 0:
                        time.sleep(delay + random.uniform(-0.1, 0.1))  # Add some jitter

            processing_time = time.time() - start_time

            stats = {
                "total_processed": self.processed_count,
                "alerts_triggered": self.alerts_triggered,
                "processing_time": round(processing_time, 2),
                "avg_time_per_tx": round(processing_time / max(self.processed_count, 1), 3),
                "status": "completed"
            }

            print("\n" + "=" * 60)
            print("✅ Stream Processing Complete")
            print(f"📈 Stats: {stats}")
            print("=" * 60)

            return stats

        except KeyboardInterrupt:
            print("\n⏹️  Stream interrupted by user")
            return {"status": "interrupted", "processed": self.processed_count}
        except Exception as e:
            print(f"\n❌ Stream error: {e}")
            return {"status": "error", "error": str(e)}
        finally:
            self.is_streaming = False

    def generate_sample_fraud_stream(self, num_transactions: int = 20) -> List[Dict[str, Any]]:
        """
        Generate a sample transaction stream with embedded fraud patterns.

        Args:
            num_transactions: Number of transactions to generate

        Returns:
            List of transaction dictionaries with fraud patterns
        """
        # Fraud patterns to include
        fraud_remarks = [
            "for goods",
            "rent payment",
            "salary transfer",
            "business payment",
            "personal loan",
            "family support",
            "friend help",
            "cash withdrawal",
            "money transfer",
            "payment received"
        ]

        accounts = [f"ACC{i:05d}" for i in range(1, 21)]  # 20 accounts
        devices = [f"DEV{i:03d}" for i in range(1, 11)]   # 10 devices

        transactions = []

        for i in range(num_transactions):
            # Create some fraud patterns
            if i % 5 == 0:  # Every 5th transaction is suspicious
                sender = random.choice(accounts[:5])  # Use same accounts for fraud
                receiver = random.choice(accounts[5:10])
                device = random.choice(devices[:3])  # Shared devices
                remark = random.choice(fraud_remarks[:3])  # Similar remarks
                amount = random.randint(50000, 200000)  # Large amounts
            else:
                sender = random.choice(accounts)
                receiver = random.choice([acc for acc in accounts if acc != sender])
                device = random.choice(devices)
                remark = random.choice(fraud_remarks)
                amount = random.randint(1000, 50000)

            tx = {
                "Transaction_ID": f"TXN{i+1:06d}",
                "sender": sender,
                "receiver": receiver,
                "amount": amount,
                "device_id": device,
                "remark": remark,
                "timestamp": datetime.now() + timedelta(seconds=i*30)  # 30s apart
            }

            transactions.append(tx)

        return transactions

    def trigger_alert(self, alert_type: str, details: Dict[str, Any]):
        """
        Trigger an alert during streaming.

        Args:
            alert_type: Type of alert (nlp, network, device, etc.)
            details: Alert details
        """
        self.alerts_triggered += 1

        alert_symbols = {
            "nlp": "🧠",
            "network": "🕸️",
            "device": "📱",
            "amount": "💰",
            "velocity": "⚡"
        }

        symbol = alert_symbols.get(alert_type, "🚨")

        print(f"{symbol} ALERT [{alert_type.upper()}]: {details}")

    def get_status(self) -> Dict[str, Any]:
        """
        Get current streaming status.

        Returns:
            Status information
        """
        return {
            "is_streaming": self.is_streaming,
            "processed_count": self.processed_count,
            "alerts_triggered": self.alerts_triggered
        }