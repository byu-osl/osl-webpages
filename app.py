from flask import Flask

app = Flask(__name__)

from views.index import index
app.register_blueprint(index)

from views.projects import projects
app.register_blueprint(projects, url_prefix="/projects")

if __name__ == '__main__': 
    app.debug = True
    app.run(host='0.0.0.0',port=8080)
