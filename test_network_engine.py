#!/usr/bin/env python
"""Test network engine get_graph_data."""
import sys
import time
sys.path.insert(0, '.')

print('Testing network engine...')
from engines.scorer import ComplianceScorer

scorer = ComplianceScorer()
print('Loading data...')
scorer.load_data()
print('Data loaded')

print('Building graph...')
scorer.network_engine.build_graph(scorer.transactions_df)
print(f'Graph built. Nodes: {scorer.network_engine.graph.number_of_nodes()}')

print('Getting graph_data...')
start = time.time()
data = scorer.network_engine.get_graph_data()
elapsed = time.time() - start
print(f'Done in {elapsed:.2f}s')
print(f'Nodes: {len(data["nodes"])}, Edges: {len(data["edges"])}')
print('First node:', data["nodes"][0] if data["nodes"] else None)
