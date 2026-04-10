from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total Requests')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        return "Hello DevOps 🚀"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}
