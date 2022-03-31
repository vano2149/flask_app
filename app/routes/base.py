"""
Базовый обработчик для
простого приложения.
"""

from app import app, db
from flask import render_template, request, redirect, flash, url_for
from app.forms.user import LoginForm, RegisterForm
from app.models.user import User
from flask_login import current_user, login_user, logout_user

"""@app.route("/login", methods=["GET","POST"])
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
        next_page = request.args.get("next")
        if not next_page:
            next_page = url_for("homepage")
        return redirect(next_page)
    return render_template("login.html", title="Log In", form=form)"""

"""@app.route("/register",methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congats! Your account created successfully!")
        return redirect(url_for("homepage"))
    return render_template("register.html", form=form, title="Register")

"""
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