from flask import Blueprint, render_template

# Blueprint is a way to organize a group of related views and other code.
bp = Blueprint('pages', __name__)

@bp.route('/')
def index():
    return render_template('pages/index.html.j2')

@bp.route('/about')
def about():
    return render_template('pages/about.html.j2')