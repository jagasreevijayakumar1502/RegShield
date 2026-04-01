#!/usr/bin/env python
"""Test all problematic endpoints to identify issues."""
import json
import sys
sys.path.insert(0, '.')
from app import app

print("=" * 70)
print("TESTING ALL PROBLEMATIC ENDPOINTS")
print("=" * 70)

with app.test_client() as client:
    # Test 1: Network Graph
    print("\n[TEST 1] GET /api/network-graph")
    print("-" * 70)
    try:
        resp = client.get('/api/network-graph')
        print(f"Status: {resp.status_code}")
        if resp.status_code != 200:
            print(f"Error: {resp.data.decode()}")
        else:
            data = resp.get_json()
            print(f"✓ Response keys: {list(data.keys())}")
            if 'nodes' in data:
                print(f"  - Nodes: {len(data['nodes'])}")
            if 'edges' in data:
                print(f"  - Edges: {len(data['edges'])}")
    except Exception as e:
        print(f"✗ Exception: {type(e).__name__}: {e}")
    
    # Test 2: STR Reports
    print("\n[TEST 2] GET /api/str-reports")
    print("-" * 70)
    try:
        resp = client.get('/api/str-reports')
        print(f"Status: {resp.status_code}")
        if resp.status_code != 200:
            print(f"Error: {resp.data.decode()}")
        else:
            data = resp.get_json()
            if isinstance(data, list):
                print(f"✓ Reports returned: {len(data)}")
                if data:
                    print(f"  - First report keys: {list(data[0].keys())}")
            else:
                print(f"✗ Unexpected response type: {type(data)}")
    except Exception as e:
        print(f"✗ Exception: {type(e).__name__}: {e}")
    
    # Test 3: Transactions
    print("\n[TEST 3] GET /api/transactions")
    print("-" * 70)
    try:
        resp = client.get('/api/transactions')
        print(f"Status: {resp.status_code}")
        if resp.status_code != 200:
            print(f"Error: {resp.data.decode()[:500]}")
        else:
            data = resp.get_json()
            if isinstance(data, list):
                print(f"✓ Transactions returned: {len(data)}")
                if data:
                    print(f"  - First record has account_info: {'account_info' in data[0]}")
            else:
                print(f"✗ Unexpected response type: {type(data)}")
    except Exception as e:
        print(f"✗ Exception: {type(e).__name__}: {e}")
    
    # Test 4: Weighted Risk
    print("\n[TEST 4] GET /api/weighted-risk")
    print("-" * 70)
    try:
        resp = client.get('/api/weighted-risk')
        print(f"Status: {resp.status_code}")
        if resp.status_code != 200:
            print(f"Error: {resp.data.decode()[:500]}")
        else:
            data = resp.get_json()
            if isinstance(data, dict):
                print(f"✓ Response keys: {list(data.keys())}")
                if 'results' in data:
                    print(f"  - Results: {len(data['results'])} accounts")
                if 'summary' in data:
                    print(f"  - Summary keys: {list(data['summary'].keys())}")
            else:
                print(f"✗ Unexpected response type: {type(data)}")
    except Exception as e:
        print(f"✗ Exception: {type(e).__name__}: {e}")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
