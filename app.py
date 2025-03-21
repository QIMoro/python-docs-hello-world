from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    f=open("prueba.txt", 'w')
    f.write("Escribo algo")
    f.close()
    return "Hola mundo (v2.0)- 21 de marzo de 2025"
