from flask import Blueprint, render_template

donate = Blueprint('donate', __name__)

@donate.route('/')
def show():
    return render_template('donate.html',active="menu-donate")
