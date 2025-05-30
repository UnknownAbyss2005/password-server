from flask import Flask, request, jsonify

app = Flask(__name__)
current_password = "InitialPassword123"

@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    if data and data.get("password") == current_password:
        return jsonify({"status": "OK"})
    return jsonify({"status": "INVALID"})

@app.route("/set_password", methods=["POST"])
def set_password():
    global current_password
    data = request.get_json()
    if data and "new_password" in data:
        current_password = data["new_password"]
        return jsonify({"status": "UPDATED"})
    return jsonify({"status": "FAILED"})
