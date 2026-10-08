#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt
)


# Création de l'application Flask
app = Flask(__name__)

# Clé secrète utilisée par Flask-JWT-Extended
# Elle permet de signer et de vérifier les JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Gestionnaire de l'authentification Basic
auth = HTTPBasicAuth()

# Gestionnaire de l'authentification JWT
jwt = JWTManager(app)


# Base de données temporaire des utilisateurs.
# Les mots de passe sont stockés sous forme de hash.
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Vérifie les identifiants envoyés avec Basic Authentication.
@auth.verify_password
def verify_password(username, password):
    """Verify a user's username and password."""
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username


# Route protégée par Basic Authentication.
# Flask-HTTPAuth appelle automatiquement verify_password().
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message for authenticated Basic Auth users."""
    return "Basic Auth: Access Granted"


# Route permettant d'obtenir un JWT.
# Le client envoie son username et son password en JSON.
@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT."""
    data = request.get_json()

    # Vérifie que le JSON reçu contient bien les identifiants.
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data["username"]
    password = data["password"]

    # Vérifie que l'utilisateur existe et que son mot de passe est correct.
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Création du JWT.
    # On place également le rôle dans le token pour pouvoir
    # effectuer ensuite le contrôle d'accès.
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )

    return jsonify({"access_token": access_token})


# Route protégée par JWT.
# Le décorateur vérifie automatiquement la présence
# et la validité du token avant d'exécuter la fonction.
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message for users with a valid JWT."""
    return "JWT Auth: Access Granted"


# Route accessible uniquement aux administrateurs.
# Le JWT doit être valide ET le rôle doit être admin.
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Return a message only for authenticated administrators."""
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# Gestion d'un JWT manquant.
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


# Gestion d'un JWT invalide.
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT errors."""
    return jsonify({"error": "Invalid token"}), 401


# Gestion d'un JWT expiré.
@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired JWT errors."""
    return jsonify({"error": "Token has expired"}), 401


# Gestion d'un JWT révoqué.
@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked JWT errors."""
    return jsonify({"error": "Token has been revoked"}), 401


# Gestion d'un token nécessitant une authentification renforcée.
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh JWT errors."""
    return jsonify({"error": "Fresh token required"}), 401


# Lance le serveur Flask lorsque le fichier est exécuté directement.
if __name__ == "__main__":
    app.run()
