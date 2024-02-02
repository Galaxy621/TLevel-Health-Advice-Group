from re import T
from connector import Connector
from flask import Blueprint, render_template, session

# Blueprint is a way to organize a group of related views and other code.
bp = Blueprint('pages', __name__)
db_connection = Connector()

@bp.route('/')
def index():
    context = {
        "title": "Home",
        "description": "Elevate your well-being with Health Advice Group, your go-to destination for expert health insights. Explore a wealth of information, expert advice, and resources to optimize your health journey. Your guide to a healthier, happier life starts here. Uncover the keys to well-being with Health Advice Group." 
    }
    return render_template('pages/index.html.j2', **context)

@bp.route('/login', methods = ["GET", "POST"])
def login():
    context = {
        "title": f"Login",
        "description": "Log in to your account to access important health information.",
    }

    session["user"] = {}
    session["loggedin"] = not session.get("loggedin", True)

    return render_template('pages/login.html.j2', **context)