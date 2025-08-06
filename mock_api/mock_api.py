from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api/create_user", methods=["POST"])
def create_user():
    data = request.json
    if not data.get("email"):
        return jsonify({"error": "Email is required"}), 400
    return jsonify({"message": "User created"}), 201


@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
