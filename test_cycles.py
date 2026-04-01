#!/usr/bin/env python
"""Test network engine get_cycles."""
import sys
import time
sys.path.insert(0, '.')

print('Testing network engine get_cycles...')
from engines.scorer import ComplianceScorer

scorer = ComplianceScorer()
print('Loading data...')
scorer.load_data()
scorer.network_engine.build_graph(scorer.transactions_df)
print(f'Graph built. Nodes: {scorer.network_engine.graph.number_of_nodes()}')

print('Getting cycles...')
start = time.time()
cycles = scorer.network_engine.get_cycles()
elapsed = time.time() - start
print(f'Done in {elapsed:.2f}s. Cycles found: {len(cycles)}')
if cycles:
    print('First cycle:', cycles[0][:5])

print('\nGetting fan_in_accounts...')
start = time.time()
fan_in = scorer.network_engine.get_fan_in_accounts()
elapsed = time.time() - start
print(f'Done in {elapsed:.2f}s. Fan-in accounts: {len(fan_in)}')
