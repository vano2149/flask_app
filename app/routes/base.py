"""
Базовый обработчик для
простого приложения.
"""

from app import app
from flask import render_template, request, redirect, flash, url_for
from app.forms.user import LoginForm
from app.models.user import User
from flask_login import current_user, login_user

@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users'))
    form = LoginForm()
    if request.method == "POST" and form.validate():
        # Пытаемся найти пользователя с таким username в бд.
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f"Invalid username or password")
            return redirect(url_for('login'))
        #Добавим пользователя в сессию.
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("users"))
    return render_template("login.html", title="Log In", form=form)

@app.route("/users", methods=["GET"])
def users():
    users = [
        {
            "username": "Alex",
            "description" : "Alex's description",
            "posts" : {
                "first" : "First super Alex's post"
            }
        },
        {
            "username" : "Bob",
            "description" : "Bob's description",
            "posts" : {
                "first" : "First super Bob's post"
            }
        },
        {
            "username" : "Alice",
            "description" : "Alice's description",
            "posts" : {
                "first" : "First super Alice's post"
            },
        }
    ]

    return render_template("users.html", users=users, username="Fedya", title="User Page")