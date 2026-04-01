"""Realistic data generator for live streaming demo."""
import random
from typing import List, Dict, Any

try:
    from faker import Faker

    _fake = Faker()
except Exception:
    _fake = None
    _names = [
        "Amit Verma",
        "Priya Nair",
        "Rohan Gupta",
        "Neha Sharma",
        "Arjun Iyer",
        "Kavya Rao",
        "Sameer Khan",
        "Meera Patil",
        "Lakshmi Menon",
        "Rahul Singh",
    ]

DEVICES = ["D1", "D2", "D3", "D4", "FRAUD_X"]
PINCODES = ["600001", "500081", "560001", "400001"]


def generate_account() -> Dict[str, Any]:
    """Create a single account with device + pincode signals."""
    return {
        "account_id": (_fake.uuid4()[:8] if _fake else f"ACC{random.randint(100000, 999999)}"),
        "name": (_fake.name() if _fake else random.choice(_names)),
        "device_id": random.choice(DEVICES),
        "pincode": random.choice(PINCODES),
        "account_age_days": random.randint(0, 5),
    }


def generate_transaction(accounts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate a transaction using existing accounts."""
    if len(accounts) < 2:
        raise ValueError("At least two accounts required to generate transactions")

    sender = random.choice(accounts)
    receiver = random.choice(accounts)

    amount = random.choice([500, 2000, 5000, 999000, 470000])
    return {
        "sender": sender["account_id"],
        "receiver": receiver["account_id"],
        "amount": amount,
        "device_id": sender["device_id"],
        "remark": random.choice(["for goods", "rent", "salary", "gift"]),
    }
