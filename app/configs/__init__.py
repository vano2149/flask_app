"""
Модуль конфигурации базового
конфигурационного приложения.
"""

import os

class Config(object):
    """
    Атрибуты соответствуют полям конфигуратора.
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "1234567890"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Исправить на валидные данные.
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    # MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_ADMIN")
    MAIL_PASSWORD = os.environ.get("EMAIL_ADMIN_PASSWIRD")

    # Postgres Глава 5.9.3 -> Путь поиска схемы.