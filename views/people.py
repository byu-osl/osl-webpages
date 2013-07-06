from flask import Blueprint, render_template

people = Blueprint('people', __name__)

@people.route('/')
def show():
    return render_template('people.html',active="menu-people")
