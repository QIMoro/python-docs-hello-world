from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mund - 21 de marzo de 2025"
