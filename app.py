from flask import Flask
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    f=open("/home/prueba.txt", 'a')
    x=datetime.datetime.now()
    f.write("Ahora son ... ", x)
    f.close()
    return "Hola mundo (v3.0)- 21 de marzo de 2025"
