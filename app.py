from flask import Flask, request, jsonify
from analyse import regression_lineaire

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    """Vérifie l’état du service."""
    return jsonify({"message": "pong"}), 200

@app.route('/analyse', methods=['POST'])
def analyse_route():
    """Exécute la régression et renvoie les coefficients."""
    data = request.get_json(force=True)
    x = data.get('x')
    y = data.get('y')
    try:
        a, b = regression_lineaire(x, y)
        return jsonify({"a": a, "b": b}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)