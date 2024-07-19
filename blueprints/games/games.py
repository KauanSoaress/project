from flask import Blueprint
from .games_defs import get_or_post_games, delete_or_edit_game, get_game_by_name

games_bp = Blueprint('games', __name__)

@games_bp.route('/games', methods=['GET', 'POST'])
def games():
    return get_or_post_games()

@games_bp.route('/games/<string:name>', methods=['GET'])
def game(name):
    return get_game_by_name(name)

@games_bp.route('/games/<string:id>', methods=['DELETE', 'PUT'])
def remove_game(id):
    return delete_or_edit_game(id)