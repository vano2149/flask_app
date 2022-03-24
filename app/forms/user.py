"""
Модуль, содержащий набор веб-форм
для взаимодействия пользователей с нашим прилодением
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """
    Класс, описывающий форму для логина пользователя.
    """
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Remembel?")
    submit = SubmitField(label="log In Button")
    