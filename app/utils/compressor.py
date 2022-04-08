"""
Функция помогающая сохранять и худеть картинки.
"""

import secrets
from app import app
import os
from PIL import Image

def save_picture(form_picture):
    """
    Функция сохранения.
    """
    random_hex = secrets.token_hex(8)
    f_ext = form_picture.filename.split('.')[-1] # Прилетает Имя нашей картинки. 
    picture_fn = random_hex + "." + f_ext # генерация нового имени файла картинки.
    picture_path = os.path.join(app.root_path, 'static/images/profiles/' + picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn
