from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///healthcare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello Fuckers"

@app.route('/<name>')
def hello_name(name):
    return "Hola {}!".format(name)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
