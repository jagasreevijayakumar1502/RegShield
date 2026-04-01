#!/usr/bin/env python
"""Test network graph endpoint."""
import sys
import json
sys.path.insert(0, '.')
from app import app

print('Testing network-graph endpoint...')
with app.test_client() as client:
    resp = client.get('/api/network-graph')
    print(f'Status: {resp.status_code}')
    if resp.status_code == 200:
        try:
            data = resp.get_json() if hasattr(resp, 'get_json') else json.loads(resp.data)
            print(f'✓ Response keys: {list(data.keys())}')
            if 'nodes' in data:
                print(f'  Nodes: {len(data["nodes"])}')
            if 'edges' in data:
                print(f'  Edges: {len(data["edges"])}')
            if 'cycles' in data:
                print(f'  Cycles: {len(data["cycles"])}')
            if 'fan_in_accounts' in data:
                print(f'  Fan-in accounts: {len(data["fan_in_accounts"])}')
        except Exception as e:
            print(f'Error parsing JSON: {e}')
            print(f'Response data (first 500 chars): {str(resp.data)[:500]}')
    else:
        print(f'✗ Error status: {resp.status_code}')
        print(f'Response: {resp.data.decode()[:500]}')
