from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    correct_password = os.environ.get("SERVER_PASSWORD", "")
    if data and data.get("password") == correct_password:
        return jsonify({"valid": True})
    return jsonify({"valid": False})

@app.route("/ping", methods=["GET"], strict_slashes=False)
def ping():
    return jsonify({"status": "alive"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)