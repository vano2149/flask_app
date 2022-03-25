"""
Модуль содержащий подробное 
описание модели User
"""

from app import db

class User(db.Model):
    """
    Модель пользователя
    согласно схеме содержать 4 атрибуда:
    * id
    * username - уникальный 
    * password_hash - закодированный пароль пользователя.
    * email - уникальный.

    еще добавим два метода для отладки: __str__, __repr__
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, prymary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    def __str__(self):
        """
        Метод отладки.
        """
        return f"User obdject (username:{self.username}, email: {self.email})"

    def __repr__(self):
        """
        Метод Отладки.
        """
        return f"<User [username:{self.username}, email:{self.email}]>"


