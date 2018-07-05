import flask
from config import Constraction
app = flask.Flask("__name__")
app.config.from_object(Constraction)