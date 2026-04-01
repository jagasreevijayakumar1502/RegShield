#!/usr/bin/env python3
"""
Quick health check for the AML system
Tests startup, endpoints, and core functionality
"""
import sys
import time
import threading
import requests


def test_app_startup():
    """Test that app starts without errors."""
    print("\n" + "="*60)
    print("🧪 AML Health Check")
    print("="*60)
    
    from app import app
    from routes.api import nlp_detector, pamrs_engine, graph_engine
    
    print("\n✅ Import check:")
    print(f"  - Flask app: OK")
    print(f"  - API blueprint: OK")
    print(f"  - NLP Detector: OK")
    print(f"  - PAMRS Engine: OK")
    print(f"  - GraphEngine: OK")
    
    return app


def start_server(app):
    """Start Flask server in background."""
    print("\n🚀 Starting Flask server...")
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)


def test_endpoints():
    """Test critical endpoints."""
    print("\n✅ Endpoint tests:")
    
    endpoints = [
        ('GET', '/api/dashboard'),
        ('GET', '/api/transactions'),
        ('GET', '/api/account/ACC00001'),
        ('GET', '/api/pamrs/ACC00001'),
        ('POST', '/api/nlp/analyze', {'transactions': [{'remark': 'for goods'}]}),
        ('GET', '/api/nlp/history'),
    ]
    
    for method, path, *data in endpoints:
        try:
            if method == 'GET':
                resp = requests.get(f'http://127.0.0.1:5000{path}', timeout=5)
            else:
                resp = requests.post(f'http://127.0.0.1:5000{path}', json=data[0], timeout=5)
            
            status = "✅" if resp.status_code < 500 else "❌"
            print(f"  {status} {method:5} {path:30} -> {resp.status_code}")
        except Exception as e:
            print(f"  ❌ {method:5} {path:30} -> ERROR: {str(e)[:40]}")


def main():
    """Main test runner."""
    try:
        app = test_app_startup()
        
        # Start server in background thread
        server_thread = threading.Thread(target=start_server, args=(app,), daemon=True)
        server_thread.start()
        
        # Wait for server to start
        print("\n⏳ Waiting for server startup...")
        time.sleep(2)
        
        # Test endpoints
        test_endpoints()
        
        print("\n" + "="*60)
        print("✅ Health check complete!")
        print("🌍 App running at: http://127.0.0.1:5000")
        print("="*60)
        
        # Keep server running
        server_thread.join()
        
    except Exception as e:
        print(f"\n❌ Health check failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
