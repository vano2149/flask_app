"""
Обработчики ошибок.
"""

from app import app
from flask import render_template

@app.errorhandler(404)
def error_404(e):
    """
    Обработчик исключения 404.
    """
    return render_template("errors/404.html", title="404 Bad Request")

@app.errorhandler(403)
def error_403(e):
    return render_template("errors/403.html", title="403 Permissions")

@app.errorhandler(500)
def error_500(e):
    return render_template("errors/500.html", title="500 Iternal Errors Server Ooops!")