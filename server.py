from flask import Flask, request, jsonify
from flask_cors import CORS
from main import run_agent

app = Flask(__name__)
CORS(app)  # ⭐ 允许跨域

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    message = data["message"]

    reply = run_agent(message)

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(port=8000)