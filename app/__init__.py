"""
Ядро приложения.
"""

from flask import Flask
from app.configs import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"
login.login_message_category = 'info'
mail = Mail(app)


from app.models.user import User
from app.models.post import Post

from app.routes.general import *
from app.routes.user import *

