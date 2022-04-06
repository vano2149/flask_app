"""
Модуль с обработчиками Post-a
"""
from app import app, db
from app.models.post import Post
from flask import render_template
from flask_login import login_required, current_user
from app.forms.post import PostForm
from flask import request, flash, redirect, url_for, abort

@app.route("/")
@app.route("/home")
def home_page():
    page = request.args.get("page", 1, type = int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=2)
    return render_template("homepage.html", title="Home Page", posts=posts)


@app.route('post/<int:id>')
@login_required
def post(id:int):
    """
    Поиск и вывод пользователя.
    """
    post = Post.query.get_or_404(id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/new", methods=["GET", "POST"])
@login_required
def post_new():
    """
    Обрабработчик создания нового поста.
    """
    form = PostForm()
    if request.method == "POST" and form.validate():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.seccion.commit()
        flash("Your post has been created!","success")
        return redirect(url_for('post', id=post.id))
    return render_template("post_new.html", title="Create New Post", form=form)


