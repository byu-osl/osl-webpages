from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)

@projects.route('/')
def show():
    return render_template('projects.html',active="menu-projects")
