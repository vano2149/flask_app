"""
Пользовательские обработчики.
"""
from app import app, db
from flask import render_template, request, redirect, flash, url_for
from app.forms.user import LoginForm, RegisterForm, UpdateUserForm, RequestResetForm, ResetPasswordForm
from app.models.user import User
from app.models.post import Post
from flask_login import current_user, login_user, logout_user, login_required
from app.utils.compressor import save_picture
from app.utils.email import send_reset_email

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

@app.route("/user/<string:username>")
@login_required
def user_public(username:str):
    """
    Публичный просмотр постов.
    """
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts= Post.query.filter_by(author=user).order_by(Post.timestamp.desc()).paginate(page=page, per_page=2)
    return render_template("user_public.html", posts=posts, user=user, title=f"{user.username}'s profile")

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_password_token():
    if current_user.is_authenticated:
        flash("You already logged in", "info")
        return redirect(url_for('home_page'))
    form = RequestResetForm()
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent with instruction to reset your password. Check Inbox", "info")
        return redirect(url_for('login'))
    return render_template("reset_password_token.html", title="Reset Password Request", form=form)

@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        flash("You already logged in", "info")
        return redirect(url_for("home_page"))
    
    user = User.verify_reset_token(token)
    if user in None:
        flash("This in an invalod or exired token", "warning")
        return redirect(url_for('reset_password_token'))
    form = ResetPasswordForm()
    if request.method == "POST" and form.valodate():
        user.set_password(form.password.data)
        db.session.commit()
        flash("New password was set. Try to log In!", "success")
        return redirect(url_for("login"))
    return render_template('reset_password.html', title="Reset Password", form=form)
