#!/usr/bin/env python3
"""
Quick PAMRS test
"""
import requests

BASE_URL = "http://localhost:5000"

def test_pamrs_real_account():
    """Test PAMRS with real account data."""
    print("Testing PAMRS with real account data...")

    try:
        response = requests.get(f"{BASE_URL}/api/pamrs/ACC00001", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ PAMRS endpoint working!")
            print(f"Account: {data['account_id']}")
            print(f"PAMRS Score: {data['pamrs_score']:.1f}/100")
            print(f"Risk Level: {data['risk_level']}")
            print(f"Recommended Action: {data['recommended_action']}")
            print("Explanation:", data['explanation'])
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    test_pamrs_real_account()