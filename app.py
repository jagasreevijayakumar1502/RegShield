"""
RegShield — Real-Time AML & Compliance Rule Engine
Flask application entry point.
"""
from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.api import api
import os

app = Flask(__name__, static_folder="static", static_url_path="/static")
CORS(app)

# Register API blueprint
app.register_blueprint(api)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/<path:path>")
def serve_static(path):
    if os.path.exists(os.path.join("static", path)):
        return send_from_directory("static", path)
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    print("=" * 60)
    print("  [RegShield] AML & Compliance Rule Engine")
    port = int(os.environ.get("PORT", "5000"))
    print(f"  Compliance Audit Portal: http://localhost:{port}")
    print("=" * 60)
    app.run(debug=True, host="0.0.0.0", port=port)
