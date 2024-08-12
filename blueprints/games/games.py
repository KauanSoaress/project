from flask import Blueprint, request
from utils.games_utils.games_defs import get_games, \
    post_games, get_game_by_name, delete_game, edit_game, get_games_by_user_id


games_bp = Blueprint('games', __name__)


@games_bp.route('/games', methods=['GET', 'POST'], endpoint='handle_games')
def handle_games():
    if request.method == 'GET':
        return get_games()
    elif request.method == 'POST':
        return post_games()


@games_bp.route('/games_by_user/<string:id>', methods=['GET'], endpoint='handle_games_by_user')
def handle_games_by_user(id):
    return get_games_by_user_id(id)


@games_bp.route('/games/<string:name>', methods=['GET'], endpoint='handle_game_by_name')
def handle_game_by_name(name):
    return get_game_by_name(name)


@games_bp.route('/games/<string:id>', methods=['DELETE', 'PUT'], endpoint='handle_game_by_id')
def handle_game_by_id(id):
    if request.method == 'DELETE':
        return delete_game(id)
    elif request.method == 'PUT':
        return edit_game(id)
