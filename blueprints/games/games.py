from flask import Blueprint, request
from utils.games_defs import get_games, post_games, get_game_by_name, delete_game, edit_game

games_bp = Blueprint('games', __name__)

@games_bp.route('/games', methods=['GET', 'POST'])
def games():
    if request.method == 'GET':
        return get_games()
    elif request.method == 'POST':
        return post_games()

@games_bp.route('/games/<string:name>', methods=['GET'])
def game(name):
    return get_game_by_name(name)

@games_bp.route('/games/<string:id>', methods=['DELETE', 'PUT'])
def remove_game(id):
    if request.method == 'DELETE':
        return delete_game(id)
    elif request.method == 'PUT':
        return edit_game(id)