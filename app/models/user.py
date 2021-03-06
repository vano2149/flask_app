"""
Модуль содержащий подробное 
описание модели User
"""

from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from datetime import datetime
from itsdangerous import TimedSerializer as Serializer


class User(UserMixin, db.Model):
    """
    Модель пользователя
    согласно схеме содержать 4 атрибуда:
    * id
    * username - уникальный 
    * password_hash - закодированный пароль пользователя.
    * email - уникальный.

    еще добавим два метода для отладки: __str__, __repr__.
    
    2 метода для работы с паролем:
        * set_password(pure_pass) - > hash_pass
        * chechk_password(semi_pure_pass) - > bool
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    image_file = db.Column(db.String(20), nullable=False, default="default.png")
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        """
        Данный метод возвращает токен для пользователя 
        с временем протухания равным expres_sec
        """
        ser = Serializer(app.config["SECRET_KEY"], expires_in=expires_sec)
        return ser.dump({'user.id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        """
        Метод проверки токена.
        """
        ser = Serializer(app.config["SECRET_KEY"])
        try:
            user_id = ser.load(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def set_password(self, pure_pass:str):
        """
        Устанавливает значение фтрибута password_hash
        при регистрации (чаще всего).
        """
        self.password_hash = generate_password_hash(pure_pass)

    
    def check_password(self, semi_pure_pass:str) -> bool:
        """
        Возвращает True если password_hash был сгенерирован на основе
        semi_pure_pass, и False в противном случае.
        """
        return check_password_hash(self.password_hash, semi_pure_pass)


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

@login.user_loader
def load_user(id:int) -> User:
    """
    Находится user в бд по ID
    """
    return User.query.get(int(id))
    
    