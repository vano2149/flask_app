"""
Модуль, содержащий набор веб-форм
для взаимодействия пользователей с нашим прилодением
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models.user import User

class LoginForm(FlaskForm):
    """
    Класс, описывающий форму для логина пользователя.
    """
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Remembel?")
    submit = SubmitField(label="log In Button")
    

class RegisterForm(FlaskForm):
    """
    Класс описывающий Регистрации потльзователя.
    """
    username = StringField(label="Username", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(),Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    password2 = PasswordField(label="Password(again)", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Register")

    """def validators_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("This username already taken.")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use different email.")"""
