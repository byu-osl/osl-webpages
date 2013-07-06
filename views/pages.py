from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)

@pages.route('/', defaults={'page': 'index'})
@pages.route('/<page>/')
def show(page):
    print "PAGE:",page
    return render_template(page+'.html',active=page)
