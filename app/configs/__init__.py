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
    