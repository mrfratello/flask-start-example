from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

apple = Flask(__name__)
apple.config.from_object('config')
db = SQLAlchemy(apple)
migrate = Migrate(apple, db)

import app.views
import app.models
