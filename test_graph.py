"""
Test Graph Engine
Quick test of the new intelligent graph engine with clustering and risk signals.
"""
from engines.network import GraphEngine

engine = GraphEngine()

transactions = [
    {"sender": "A", "receiver": "B", "amount": 1000, "device_id": "D1"},
    {"sender": "B", "receiver": "C", "amount": 2000, "device_id": "D1"},
    {"sender": "C", "receiver": "D", "amount": 3000, "device_id": "D1"},
    {"sender": "X", "receiver": "Y", "amount": 500, "device_id": "D2"},
]

engine.build_graph(transactions)

print("Clusters:", engine.detect_clusters())
print("Suspicious:", engine.get_suspicious_clusters())
print("Hubs:", engine.get_hub_accounts())
print("Device Clusters:", engine.detect_device_clusters())
print("Summary:", engine.get_graph_summary())