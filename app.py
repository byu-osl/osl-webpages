import sys

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'

@app.route('/')
def index():
    return render_template('index.html',active='index')

@app.route('/<directory>',defaults={'page':''})
@app.route('/<directory>/<page>')
def show(directory,page):
    if not page:
        return render_template(directory+'.html',active=directory)
    return render_template(directory+"/" + page + '.html',active=directory)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8080)
