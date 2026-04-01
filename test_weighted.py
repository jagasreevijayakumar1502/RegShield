#!/usr/bin/env python
"""Test weighted risk endpoint."""
import sys
import json
sys.path.insert(0, '.')
from app import app

print('Testing weighted-risk endpoint...')
with app.test_client() as client:
    resp = client.get('/api/weighted-risk')
    print(f'Status: {resp.status_code}')
    if resp.status_code == 200:
        try:
            data = resp.get_json() if hasattr(resp, 'get_json') else json.loads(resp.data)
            print(f'✓ Response keys: {list(data.keys())}')
            print(f'  Results: {len(data["results"])} accounts')
            print(f'  Summary keys: {list(data["summary"].keys())}')
            if data['results']:
                print(f'  First result keys: {list(data["results"][0].keys())}')
        except Exception as e:
            print(f'Error parsing JSON: {e}')
    else:
        print(f'✗ Error: {resp.data.decode()[:500]}')

