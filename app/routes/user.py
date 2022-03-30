"""
Пользовательские обработчики.
"""
from app import app, db
from flask import render_template, request, redirect, flash, url_for
from app.forms.user import LoginForm, RegisterForm
from app.models.user import User
from flask_login import current_user, login_user, logout_user

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        if form.email.data == "admin@admin.com" and form.password.data == "admin":
            flash('You have been logged in!', 'success')
            return redirect(url_for("home_page"))
        else:
            flash('Login Unsuccessfull. Please check your email and password! ', 'danger')

    return render_template("login.html", title="login", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home_page'))
    return render_template("register.html", title="Register", form=form)
