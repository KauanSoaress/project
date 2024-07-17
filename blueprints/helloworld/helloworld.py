from flask import Blueprint, render_template, redirect

helloworld_bp = Blueprint('helloworld', __name__)

@helloworld_bp.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@helloworld_bp.route("/hello", methods=['GET'])
def hello():
    return "Hello"

@helloworld_bp.route("/hello/<string:name>", methods=['GET'])
def say_hello(name):
    return f"Hello, {name}"