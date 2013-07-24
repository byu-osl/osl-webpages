import sys

from flask import Flask, render_template
from flask_frozen import Freezer

analytics = ""
try:
    from config import analytics
except:
    pass

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html',active='index',analytics=analytics)

@app.route('/<page>/')
def show(page):
    print "PAGE:",page
    return render_template(page+'.html',active=page,analytics=analytics)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8080)
