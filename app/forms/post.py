"""
Форма Post.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class PostForm(FlaskForm):
    """
    Клвсс описывающий форму поста пользователя.
    """
    title = StringField(label='Title', validators=[DataRequired()])
    content = TextAreaField(label="Content", validators=[DataRequired()])
    submit = SubmitField(label="Create Post")

class AddCommetnForm(FlaskForm):
    """
    Класс описывающий форму коментария к посту.
    """
    body = StringField(label="Body", validators=[InputRequired()])
    submit = SubmitField(label="Create Comment")
