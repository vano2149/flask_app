"""
Обработчик начальной стр.
И страници about.
"""

from app import app
from flask import render_template , request
from flask_login import login_required
from app.models.post import Post, posts # это не этот posts определяется в home_page function.
from app.models.user import User

@app.route("/")
@app.route("/home")
def home_page():
    page = request.args.get("page", 1, type = int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=2)
    return render_template("homepage.html", title="Home Page", posts=posts)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About Page")

@app.route("/user/<string:username>")
@login_required
def user_public(username:str):
    """
    Публичный просмотр постов.
    """
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts= Post.query.filter(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template("user_public.html", posts=posts, user=user, title=f"{user.username}'s profile")
