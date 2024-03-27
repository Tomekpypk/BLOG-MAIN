import os

class Config:
    
    SECRET_KEY = '5749372817563927'

    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Tomek")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "blogasylogasy")

    # BAZA NA PRZYSZŁOŚĆ
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    POSTS_PER_PAGE = 10  # Ilość postów na stronę
