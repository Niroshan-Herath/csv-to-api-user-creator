from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)


# Define an API endpoint to handle user creation via POST
@app.route("/api/create_user", methods=["POST"])
def create_user():
    data = request.json  # Get JSON data sent in the request body

    # Validate that 'email' is present in the request
    if not data.get("email"):
        return jsonify({"error": "Email is required"}), 400
    return jsonify({"message": "User created"}), 201


# Health check endpoint used to verify if the API is running
@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
