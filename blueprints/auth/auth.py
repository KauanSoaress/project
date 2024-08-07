from flask import Blueprint, make_response, jsonify
from flask_security import auth_required, permissions_accepted

auth_bp = Blueprint('auth', __name__)

# Views
@auth_bp.route("/")
def home():
    return make_response(jsonify(message="Hello World!"))

@auth_bp.route("/user")
@auth_required(['basic', 'session'])
@permissions_accepted("user-read")
def user_home():
    return make_response(jsonify(message="Hello User!"))