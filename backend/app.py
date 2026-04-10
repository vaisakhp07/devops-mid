from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

start_time = time.time()

@app.route("/")
def home():
    return "DevOps Project Backend Running......fdghjghgfd"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/users")
def users():
    sample_users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    return jsonify(sample_users)

@app.route("/metrics")
def metrics():
    uptime = time.time() - start_time
    return f"""
# HELP app_uptime_seconds Uptime of the app
# TYPE app_uptime_seconds counter
app_uptime_seconds {uptime}

# HELP random_value Random metric
# TYPE random_value gauge
random_value {random.randint(1,100)}
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
