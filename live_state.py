"""Shared in-memory state for live streaming demo."""
from collections import deque
from typing import Dict, Any, List

# Rolling stores
accounts: List[Dict[str, Any]] = []
alerts: deque = deque(maxlen=50)
transactions: deque = deque(maxlen=100)


def get_state() -> Dict[str, Any]:
    """Return a snapshot of the current live state."""
    return {
        "accounts": list(accounts),
        "alerts": list(alerts),
        "transactions": list(transactions),
    }
