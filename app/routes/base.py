"""
Базовый обработчик для
простого приложения.
"""

from app import app
from flask import render_template, request, redirect, flash, url_for
from app.forms.user import LoginForm


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        flash(f"Login requests form user {form.username.data} with password {form.password.data}")
        return redirect(url_for("users"))

    return render_template("login.html", title = "Log In", form=form, username="Vasya")

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