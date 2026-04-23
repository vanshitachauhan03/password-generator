from flask import Blueprint, request, jsonify, current_app
from .generator import generate_password
from .entropy import calculate_entropy, strength_label

main = Blueprint("main", __name__)

@main.route("/generate", methods=["POST"])
def generate():
    data = request.json or {}

    # Use config default if not provided
    length = data.get(
        "length",
        current_app.config["DEFAULT_PASSWORD_LENGTH"]
    )

    password = generate_password(length=length)
    entropy = calculate_entropy(password)
    strength = strength_label(entropy)

    return jsonify({
        "password": password,
        "entropy": round(entropy, 2),
        "strength": strength
    })