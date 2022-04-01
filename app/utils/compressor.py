"""
Функция помогающая сохранять и худеть картинки.
"""

import secrets
from app import app

def save_picture(form_picture):
    """
    Функция сохранения.
    """
    random_hex = secrets.token_hex(8)
    f_ext = form_picture.filename.split('.')[-1] # Прилетает Имя нашей картинки. 
    