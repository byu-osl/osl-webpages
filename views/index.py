from flask import Blueprint, render_template

### Home Page ### 

index = Blueprint('index', __name__)

@index.route('/')
def show():
    return render_template('index.html',active="menu-home")
