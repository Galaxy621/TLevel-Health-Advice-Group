from flask import Flask
from webapp import pages
from config import Config

from flask_mysqldb import MySQL

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql = MySQL(app)

    app.register_blueprint(pages.bp)
    return app