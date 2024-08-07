from flask import Blueprint, request
from utils.games_utils.games_defs import get_games, post_games, get_game_by_name, delete_game, edit_game
from flask_security import auth_required, permissions_accepted

games_bp = Blueprint('games', __name__)

@games_bp.route('/games', methods=['GET', 'POST'], endpoint='handle_games')
@auth_required(['basic', 'session'])
@permissions_accepted("user-read", "user-write")
def handle_games():
    if request.method == 'GET':
        return get_games()
    elif request.method == 'POST':
        return post_games()

@games_bp.route('/games/<string:name>', methods=['GET'], endpoint='handle_game_by_name')
@auth_required(['basic', 'session'])
@permissions_accepted("user-read")
def handle_game_by_name(name):
    return get_game_by_name(name)

@games_bp.route('/games/<string:id>', methods=['DELETE', 'PUT'], endpoint='handle_game_by_id')
@auth_required(['basic', 'session'])
@permissions_accepted("user-write")
def handle_game_by_id(id):
    if request.method == 'DELETE':
        return delete_game(id)
    elif request.method == 'PUT':
        return edit_game(id)