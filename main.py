import os
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "LINA Signal Server ishlayapti!"

@app.route('/signal', methods=['POST'])
def receive_signal():
    content = request.json.get("content", "")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("context.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n{content}\n")
    return jsonify({"status": "success", "message": "Signal qabul qilindi."})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render `PORT` muhit o‘zgaruvchisini o‘qiydi
    app.run(host="0.0.0.0", port=port)
