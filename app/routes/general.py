"""
Обработчик начальной стр.
И страници about.
"""

from app import app
from flask import render_template
from flask_login import login_required

@app.route("/", methods=["GET"])
def home_page():
    return render_template("homepage.html", title="Home Page")

@app.route("/about", methods=["GET"])
@login_required
def about():
    return render_template("about.html", title="About Page")

