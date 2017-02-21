from flask import Flask
from flask_sqlalchemy import SQLAlchemy

apple = Flask(__name__)
apple.config.from_object('config')
db = SQLAlchemy(apple)
import app.views
import app.models
