"""
Модуль подключения, 
отправки сообщений на email.
"""
from app import mail
from flask import url_for
from flask_mail import Message

def send_reset_email(user):
    """
    Функция отправки формы для сброса пароля.
    """
    token = user.get_reset_token()
    msg = Message("Password Reset Request", sender=app.config['MAIL_USERNAME'], recipients=[user.email])
    msg.body = f"""
    To reset your password visit the following link:
    {url_for('reset_password', token=token, _external=True)}
    If you did't make this requests then simply ignore this message.

    Regards,
    My Flask Blog Team.
    """
    mail.send(msg)