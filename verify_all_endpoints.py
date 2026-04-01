#!/usr/bin/env python
"""Final verification of all endpoints."""
import requests
import sys

BASE_URL = "http://localhost:5000"

print("=" * 70)
print("FINAL ENDPOINT VERIFICATION")
print("=" * 70)

results = {}
endpoints = [
    ("/api/dashboard", 30),
    ("/api/network-graph", 10),
    ("/api/str-reports", 10),
    ("/api/weighted-risk", 10),
    ("/api/transactions", 30),
]

for endpoint, timeout in endpoints:
    print(f"\n[TEST] GET {endpoint}")
    try:
        resp = requests.get(f"{BASE_URL}{endpoint}", timeout=timeout)
        status = "✓" if resp.status_code == 200 else "✗"
        print(f"  {status} Status: {resp.status_code}")
        results[endpoint] = resp.status_code == 200
        if resp.status_code == 200:
            try:
                data = resp.json()
                if isinstance(data, list):
                    print(f"    Response: list ({len(data)} items)")
                elif isinstance(data, dict):
                    print(f"    Response: dict ({list(data.keys())[:3]}...)")
            except:
                print(f"    Response: {resp.text[:100]}")
    except requests.exceptions.Timeout:
        print(f"  ✗ Timeout after {timeout}s")
        results[endpoint] = False
    except Exception as e:
        print(f"  ✗ Error: {type(e).__name__}: {str(e)[:80]}")
        results[endpoint] = False

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
passed = sum(1 for v in results.values() if v)
total = len(results)
print(f"\nPassed: {passed}/{total}")
for endpoint, success in results.items():
    status = "✓" if success else "✗"
    print(f"  {status} {endpoint}")

sys.exit(0 if passed == total else 1)
