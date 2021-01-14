from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from config import Config
from models import User, Role

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/healthcare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello():
    return "Hello Fuckers"

@app.route('/<name>')
def hello_name(name):
    return "Hola {}!".format(name)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
