#!/usr/bin/env python
"""Quick test of endpoints."""
import requests
import json

BASE_URL = "http://localhost:5000"

print("=" * 70)
print("TESTING ENDPOINTS")
print("=" * 70)

with requests.Session() as session:
    # Test 1: Dashboard
    print("\n[1] Testing GET /api/dashboard...")
    try:
        resp = session.get(f"{BASE_URL}/api/dashboard", timeout=30)
        print(f"✓ Status: {resp.status_code}")
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {e}")
    
    # Test 2: Network Graph
    print("\n[2] Testing GET /api/network-graph...")
    try:
        resp = session.get(f"{BASE_URL}/api/network-graph", timeout=10)
        print(f"✓ Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"  Keys: {list(data.keys())}")
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {e}")
    
    # Test 3: STR Reports
    print("\n[3] Testing GET /api/str-reports...")
    try:
        resp = session.get(f"{BASE_URL}/api/str-reports", timeout=10)
        print(f"✓ Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, list):
                print(f"  Type: list, Length: {len(data)}")
            else:
                print(f"  Response type: {type(data).__name__}")
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {e}")
    
    # Test 4: Weighted Risk
    print("\n[4] Testing GET /api/weighted-risk...")
    try:
        resp = session.get(f"{BASE_URL}/api/weighted-risk", timeout=10)
        print(f"✓ Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"  Keys: {list(data.keys())}")
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {e}")
    
    # Test 5: Transactions
    print("\n[5] Testing GET /api/transactions...")
    try:
        resp = session.get(f"{BASE_URL}/api/transactions", timeout=30)
        print(f"✓ Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, list):
                print(f"  Type: list, Length: {len(data)}")
                if data:
                    print(f"  Sample keys: {list(data[0].keys())[:5]}")
            else:
                print(f"  Response type: {type(data).__name__}")
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {e}")

print("\n" + "=" * 70)
