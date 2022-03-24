"""
Ядро приложения.
"""

from flask import Flask
from app.configs import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.routes import base