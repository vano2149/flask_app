"""
Пользовательские обработчики.
"""
from app import app, db
from flask import render_template, request, redirect, flash, url_for
from app.forms.user import LoginForm, RegisterForm
from app.models.user import User
from flask_login import current_user, login_user, logout_user


@app.route("/logout", methods=["GET"])
def logout():
    flash("User successfuly logged out!")
    logout_user()
    return redirect(url_for("users"))

@app.route("/login", methods=["GET","POST"])
def login():
    """
    Обработчик Login-a пользователя.
    """
    if current_user.is_authenticated:
        flash("You already logged in", "info")
        return redirect(url_for("home"))
    form = LoginForm()
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember_me=form.remember_me.data)
            flash('You have been logged in!','success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccsesfull. Please check your email and password!','danger')
    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You already logged in", 'info')
        return redirect(url_for("home"))
    form = RegisterForm
    if request.method == 'POST' and form.validate():
        user = User(username=form.usermname.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}! Try to log In!", 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/account", methods=["GET","POST"])
def account():
    image_file = url_for('static', filename="images/profiles/" + current_user.image_file)
    return render_template("account.html", title="My Account", image_file=image_file)