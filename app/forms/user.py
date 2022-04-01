"""
Модуль, содержащий набор веб-форм
для взаимодействия пользователей с нашим прилодением
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models.user import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class UpdateUserForm(FlaskForm):
    """
    Класс описывающий форму изменения данных пользователя.
    """
    username = StringField(label="Username" , validators=[DataRequired(), Length(3, 64)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    picture = FileField(label="Update Profile Picture", validators=[FileAllowed(['png','jpg','jpeg'])])
    submit =SubmitField(label='Edit')

    def validators_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter(User.username == username).first()
            if user:
                raise ValidationError("That username is taken. Please choose a different one!")
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken.Please choose a different one!")


class LoginForm(FlaskForm):
    """
    Класс, описывающий форму для логина пользователя.
    """
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Remember Me?")
    submit = SubmitField(label="log In")
    

class RegisterForm(FlaskForm):
    """
    Класс описывающий Регистрации потльзователя.
    """
    username = StringField(label="Username", validators=[DataRequired(), Length(3, 64)])
    email = StringField(label="Email", validators=[DataRequired(),Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    confirm_password = PasswordField(label="Password(again)", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Sing Up")


