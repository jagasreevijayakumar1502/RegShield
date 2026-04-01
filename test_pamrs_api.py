#!/usr/bin/env python3
"""
Test PAMRS API endpoints
"""
import requests
import json

BASE_URL = "http://localhost:5000"


def _print_ok(msg: str):
    print(f"[OK] {msg}")


def _print_err(msg: str):
    print(f"[ERR] {msg}")


def test_pamrs_endpoint():
    """Test PAMRS scoring for an existing account."""
    print("Testing PAMRS endpoint for existing account...")

    try:
        response = requests.get(f"{BASE_URL}/api/pamrs/ACC00001", timeout=10)
        if response.status_code == 200:
            data = response.json()
            _print_ok("PAMRS endpoint working!")
            print(f"Account: {data['account_id']}")
            print(f"PAMRS Score: {data['pamrs_score']:.1f}/100")
            print(f"Risk Level: {data['risk_level']}")
            print(f"Recommended Action: {data['recommended_action']}")
            print(f"Explanation: {data['explanation']}")
        else:
            _print_err(f"HTTP {response.status_code} - {response.text}")
    except Exception as e:
        _print_err(f"Connection error: {e}")


def test_pamrs_new_account():
    """Test PAMRS scoring for a new account."""
    print("\nTesting PAMRS endpoint for new account...")

    # /api/accounts requires these fields: Account_ID, Customer_ID, Device_ID, Pincode, Account_Created_Date
    new_account = {
        "Account_ID": "NEW_ACC_TEST",
        "Customer_ID": "CUST_TEST_001",
        "Device_ID": "DEV_TEST_123",
        "Pincode": "400001",  # Low risk pincode
        "Account_Created_Date": "2024-01-15"
    }

    try:
        # Use the real account-creation endpoint which also returns PAMRS details
        response = requests.post(f"{BASE_URL}/api/accounts", json=new_account, timeout=10)
        if response.status_code in (200, 201):
            data = response.json()
            _print_ok("New account PAMRS working!")
            print(f"Account: {data.get('account_id') or new_account['Account_ID']}")
            print(f"PAMRS Score: {data.get('pamrs_score', 0):.1f}/100")
            print(f"Risk Level: {data.get('risk_level')}")
            print(f"Recommended Action: {data.get('recommended_action')}")
        else:
            _print_err(f"HTTP {response.status_code} - {response.text}")
    except Exception as e:
        _print_err(f"Connection error: {e}")


def test_dashboard():
    """Test dashboard with PAMRS statistics."""
    print("\nTesting dashboard with PAMRS statistics...")

    try:
        # First dashboard call can take longer because it loads data and runs scorers
        response = requests.get(f"{BASE_URL}/api/dashboard", timeout=30)
        if response.status_code == 200:
            data = response.json()
            if "pamrs_distribution" in data:
                _print_ok("Dashboard includes PAMRS statistics!")
                pamrs_dist = data["pamrs_distribution"]
                print(
                    f"PAMRS Distribution: Low={pamrs_dist['low']}, "
                    f"Medium={pamrs_dist['medium']}, "
                    f"High={pamrs_dist['high']}, "
                    f"Total={pamrs_dist['total_evaluated']}"
                )
            else:
                _print_err("PAMRS statistics not found in dashboard")
        else:
            _print_err(f"HTTP {response.status_code} - {response.text}")
    except Exception as e:
        _print_err(f"Connection error: {e}")


if __name__ == "__main__":
    print("Testing PAMRS API Integration...")
    test_pamrs_endpoint()
    test_pamrs_new_account()
    test_dashboard()
    print("\nPAMRS API testing complete!")
