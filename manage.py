"""
Входная точка 
для запуска приложения.
"""

from app import app

@app.shell_context_processor
def make_shell_context():
    """
    Возвращает словарь для flask shell
    где ключ - это короткое имя, через которое можно получить 
    доступ к объекту (value) возвращенного словаря.
    """
    return {
        "app" : app,
    }
if __name__ == "__main__":
    app.run(port=8080, debug=True)