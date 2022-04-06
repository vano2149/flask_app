"""
Обработчик начальной стр.
И страници about.
"""

from app import app
from flask import render_template , request
from flask_login import login_required
from app.models.post import Post # это не этот posts определяется в home_page function.
from app.models.user import User


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About Page")
