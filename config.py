"""Module for set the configuration of enviroment Flask"""

from decouple import config
from os.path import join, dirname

USER = config("USER")
HOST = config("HOST")
PASSWORD = config("PASSWORD")


def set_db_connect(db_name):
    """set the credentials for connect to db"""

    return f'mysql://{USER}:{PASSWORD}@{HOST}/{db_name}'


class DefaultConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = set_db_connect('flask')
    SQLALCHEMY_BINDS = {
        'products_ms': set_db_connect('products_ms'),
        'users_ms': set_db_connect('users_ms'),
    }


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SECRET_KEY = 'dev'


class ProductionConfig(DefaultConfig):
    SECRET_KEY = config("SECRET_KEY")
