from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
SAVE_DIR = "signal_logs"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route('/')
def home():
    return 'LINA signal server is active!'

@app.route('/receive_signal', methods=['POST'])
def receive_signal():
    data = request.get_json()
    signal_type = data.get("signal_type")
    content = data.get("content")
    source = data.get("source", "unknown")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{SAVE_DIR}/signal_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Type: {signal_type}\nSource: {source}\nTime: {timestamp}\n\n{content}")

    return jsonify({"message": "Signal received successfully!"}), 200
