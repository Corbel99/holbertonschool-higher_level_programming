#!/usr/bin/python3

from flask import Flask, jsonify, request

# Création de l'application Flask
app = Flask(__name__)

# Dictionnaire contenant les utilisateurs
# La clé est le username et la valeur est le dictionnaire de l'utilisateur
users = {
    "jane": {
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


# Route principale de l'API
@app.route("/")
def home():
    """Retourne le message d'accueil de l'API."""
    return "Welcome to the Flask API!"


# Route qui retourne la liste des usernames
@app.route("/data")
def data():
    """Retourne tous les usernames sous forme de JSON."""
    return jsonify(list(users.keys()))


# Route qui vérifie le statut de l'API
@app.route("/status")
def status():
    """Retourne le statut de l'API."""
    return "OK"


# Route dynamique permettant de rechercher un utilisateur
@app.route("/users/<username>")
def user(username):
    """Retourne les informations d'un utilisateur."""
    # Vérifie si le username existe comme clé dans users
    if username in users:
        # Récupère le dictionnaire associé au username
        return jsonify(users[username])
    else:
        # L'utilisateur n'existe pas : retourne une erreur 404
        return jsonify({"error": "User not found"}), 404


# Route permettant d'ajouter un utilisateur avec une requête POST
@app.route("/add_user", methods=["POST"])
def add_user():
    """Ajoute un nouvel utilisateur à l'API."""
    # Récupère les données JSON envoyées par le client
    data = request.get_json()

    # Vérifie si le JSON est valide
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Vérifie que le username est présent
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # Récupère le username envoyé
    username = data["username"]

    # Vérifie si ce username existe déjà
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Ajoute le nouvel utilisateur dans le dictionnaire users
    users[username] = data

    # Retourne une confirmation avec les données du nouvel utilisateur
    # 201 signifie que l'utilisateur a été créé
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


# Lance le serveur Flask lorsque le fichier est exécuté directement
if __name__ == "__main__":
    app.run()
