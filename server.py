from flask import Flask, request, jsonify
import os

app = Flask(__name__)
current_password = "attendance"

@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    if data and data.get("password") == current_password:
        return jsonify({"valid": True})
    return jsonify({"valid": False})

@app.route("/set_password", methods=["POST"])
def set_password():
    global current_password
    data = request.get_json()
    if data and "new_password" in data:
        current_password = data["new_password"]
        return jsonify({"status": "UPDATED"})
    return jsonify({"status": "FAILED"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)