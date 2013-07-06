from flask import Flask, render_template

app = Flask(__name__)

from views.pages import pages
app.register_blueprint(pages)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__': 
    app.debug = True
    app.run(host='0.0.0.0',port=8080)
