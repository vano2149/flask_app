"""
Пользовательские обработчики.
"""
from app import app, db
from flask import render_template, request, redirect, flash, url_for
from app.forms.user import LoginForm, RegisterForm, UpdateUserForm
from app.models.user import User
from flask_login import current_user, login_user, logout_user, login_required
from app.utils.compressor import save_picture

@app.route("/logout", methods=["GET"])
def logout():
    flash("User successfuly logged out!")
    logout_user()
    return redirect(url_for("home_page"))

@app.route("/account", methods=["GET","POST"])
@login_required
def account():
    form = UpdateUserForm()
    if request.method == "POST" and form.validate():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account info updated!", "success")
        return redirect(url_for("account"))
    else:
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename="images/profiles/" + current_user.image_file)
    return render_template("account.html", title="My Account", image_file=image_file, form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    """
    Обработчик Login-a пользователя.
    """
    if current_user.is_authenticated:
        flash("You already logged in", "info")
        return redirect(url_for("home_page"))
    form = LoginForm()
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You have been logged in!','success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home_page'))
        else:
            flash('Login Unsuccsesfull. Please check your email and password!','danger')
    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You already logged in", 'info')
        return redirect(url_for("home_page"))
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}! Try to log In!", 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)


