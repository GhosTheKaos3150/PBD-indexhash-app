from flask import Blueprint

index_route = Blueprint("index", __name__)

@index_route.route("/")
def index():
    return "RELO UOUDI"

@index_route.route("/echo/<word>")
def echo(word):
    return f"<h1>{word}</h1>"
