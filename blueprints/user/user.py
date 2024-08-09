from flask import Blueprint, request
from utils.user_utils.user_defs import get_user, post_user, get_user_by_id, get_user_by_name, delete_user, edit_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['GET', 'POST'], endpoint='handle_user')
def handle_user():
    if request.method == 'GET':
        return get_user()
    elif request.method == 'POST':
        return post_user()
    
@user_bp.route('/user/<string:id>', methods=['GET', 'DELETE', 'PUT'], endpoint='handle_user_by_id')
def handle_user_by_id(id):
    if request.method == 'GET':
        return get_user_by_id(id)
    elif request.method == 'DELETE':
        return delete_user(id)
    elif request.method == 'PUT':
        return edit_user(id)
