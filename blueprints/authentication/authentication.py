from flask import Blueprint
from utils.auth_utils.auth_defs import register, login

auth_bp = Blueprint('games', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    return register()

@auth_bp.route('/login', methods=['GET'])
def login():
    return login()