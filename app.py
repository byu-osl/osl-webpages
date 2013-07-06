from flask import Flask

app = Flask(__name__)

from views.index import index
app.register_blueprint(index)

from views.projects import projects
app.register_blueprint(projects, url_prefix="/projects")

from views.people import people
app.register_blueprint(people, url_prefix="/people")

from views.donate import donate
app.register_blueprint(donate, url_prefix="/donate")

if __name__ == '__main__': 
    app.debug = True
    app.run(host='0.0.0.0',port=8080)
