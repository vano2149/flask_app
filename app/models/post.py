"""
Модуль содержаший детальное
описание
модели Post.
"""

from app import db
from datetime import datetime

class Post(db.Model):
    """
    Модель поста 
    согласно схеме содержит 4 атрибута:
    * id - индентификатор поста.
    * body - тело поста.
    * timestamp - время создания поста.
    * user_id - идентификатор пользователя из таблици users.

    еще добавим два метода отладки: __str__, __repr__
    """

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(450))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __str__(self):
        return f"Post object (timrstamp:{self.timestamp}, body:{self.body})"
    
    def __repr__(self):
        return f"<Post [timestamp:{self.timestamp}, body:{self.body}]>"

posts = [
    {
        "author" : "Ivan Kal'ko",
        'title' : 'Blog Post #1',
        'content' : "First post content",
        'date_posted' : "March 13, 2022",
    },
    {
        'author' : 'Alice Yandex',
        'title' : 'Blog Post #2',
        'content': 'Second post content',
        'date_posted' : 'March 10, 2022',
    },
    {
        'author':"Dungeon Master",
        'title':'Blog Post #3',
        'content' :'Third post content',
        'date_posted': 'April 28, 2022',
    }
]