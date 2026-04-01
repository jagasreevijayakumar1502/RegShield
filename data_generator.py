"""Realistic synthetic data generator for live fraud demos."""
import random
import time
from typing import List, Dict

try:
    from faker import Faker
    fake = Faker()
except Exception:
    fake = None
    _names = [
        "Amit Verma", "Priya Nair", "Rohan Gupta", "Neha Sharma",
        "Arjun Iyer", "Kavya Rao", "Sameer Khan", "Meera Patil",
        "Lakshmi Menon", "Rahul Singh",
    ]

# Shared device pool for normal traffic
devices = ["D1", "D2", "D3", "D4"]


def generate_account() -> Dict[str, str]:
    """Create a single synthetic account with light risk signals."""
    return {
        "account_id": (fake.uuid4()[:8] if fake else f"ACC{random.randint(100000,999999)}"),
        "name": (fake.name() if fake else random.choice(_names)),
        "pincode": random.choice(["600001", "500081", "560001", "400001"]),
        "device_id": random.choice(devices),
        "account_age_days": random.randint(0, 10),
    }


def generate_transaction(accounts: List[Dict[str, str]]) -> Dict[str, str]:
    """Create a transaction between two existing accounts."""
    if not accounts:
        raise ValueError("No accounts available to generate transactions.")

    sender = random.choice(accounts)
    receiver = random.choice(accounts)

    tx_amount = random.choice([500, 1000, 5000, 999000, 470000])
    # Structuring / smurfing pattern: occasionally max out at ₹9.99L
    if random.random() < 0.2:
        tx_amount = 999000

    return {
        "sender": sender["account_id"],
        "receiver": receiver["account_id"],
        "amount": tx_amount,
        "device_id": sender["device_id"],
        "remark": random.choice(["for goods", "rent payment", "salary", "gift"]),
        "timestamp": time.time(),
    }


def generate_mule_cluster(accounts: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Create coordinated mule accounts that all share one device."""
    device = "FRAUD_DEVICE"
    new_accounts: List[Dict[str, str]] = []

    for _ in range(5):
        acc = generate_account()
        acc["device_id"] = device  # Same device -> high risk cluster
        new_accounts.append(acc)

    accounts.extend(new_accounts)
    return new_accounts
