from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    correct_password = os.environ.get("SERVER_PASSWORD", "")
    device_id = data.get("device_id", "unknown") if data else "unknown"
    ip_address = request.remote_addr

    # Format: 2025-06-09 19:12:45 - abc123 - 1.2.3.4
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {device_id} - {ip_address}\n"

    with open("access_log.txt", "a") as log_file:
        log_file.write(log_entry)

    if data and data.get("password") == correct_password:
        return jsonify({"valid": True})
    return jsonify({"valid": False})

@app.route("/ping", methods=["GET"], strict_slashes=False)
def ping():
    return jsonify({"status": "alive"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)