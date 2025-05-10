from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "LINA Signal Server ishga tushdi!"

@app.route('/signal', methods=['POST'])
def receive_signal():
    content = request.json.get("content", "")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("context.txt", "w", encoding="utf-8") as f:
        f.write(f"{timestamp}\n{content}")
    return jsonify({"status": "success", "message": "Signal qabul qilindi."})
