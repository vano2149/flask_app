"""
Ядро приложения.
"""

from flask import Flask
from app.configs import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


from app.routes import base
from app.routes import general
from app.models.user import User
from app.models.post import Post
