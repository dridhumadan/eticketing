from flask import Flask
from mongoengine import connect

app = Flask(__name__)

connect('eticketing')

from eticketing.errors.handlers import errors
from eticketing.home.routes import home

app.register_blueprint(errors)
app.register_blueprint(home)
