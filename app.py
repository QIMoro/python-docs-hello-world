from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo (v2.0)- 21 de marzo de 2025"
