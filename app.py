from flask import Flask, jsonify
import os

app = Flask(__name__)

# TODO: move to env variable (see SECURITY.md)
SECRET_KEY = "supersecret123"

@app.route("/")
def home():
    return jsonify({
        "message": "Npontu DevOps Pipeline - Running",
        "status": "healthy"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
