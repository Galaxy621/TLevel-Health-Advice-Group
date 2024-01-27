import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'password'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'db'
    MYSQL_CURSORCLASS = 'DictCursor'