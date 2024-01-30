from flask import Blueprint, render_template

# Blueprint is a way to organize a group of related views and other code.
bp = Blueprint('pages', __name__)

@bp.route('/')
def index():
    context = {
        "title": "Home",
        "description": "Elevate your well-being with Health Advice Group, your go-to destination for expert health insights. Explore a wealth of information, expert advice, and resources to optimize your health journey. Your guide to a healthier, happier life starts here. Uncover the keys to well-being with Health Advice Group." 
    }
    return render_template('pages/index.html.j2', **context)