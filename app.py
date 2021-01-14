from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello Fuckers"

@app.route('/<name>')
def hello_name(name):
    return "Hola {}!".format(name)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
