from flask import Blueprint, render_template, redirect
from flask import jsonify, request, make_response
import json

games_bp = Blueprint('games', __name__)

@games_bp.route('/games', methods=['GET'])
def get_games():
    data = open('bd.json')
    games = json.load(data)
    data.close()
    
    return make_response(
        jsonify(
            message= 'Games list', 
            game= games
        )
    )

@games_bp.route('/games/<string:name>', methods=['GET'])
def get_game(name):
    data = open('bd.json')
    games = json.load(data)

    for game in games:
        if game['name'] == name:
            return make_response (
                jsonify(
                    message= 'Game found', 
                    game= game
                )
            )
        
@games_bp.route('/games', methods=['POST'])
def post_game():
    data = open('bd.json')
    games = json.load(data)
    data.close()

    new_game = request.get_json()
    games.append(new_game)

    data = open('bd.json', 'w')
    json.dump(games, data, indent=4)
    data.close()

    return make_response(
        jsonify(
            message= 'Game created', 
            game= new_game
        )
    )

@games_bp.route('/games/<int:id>', methods=['DELETE'])
def delete_game(id):
    data = open('bd.json')
    games = json.load(data)
    data.close()

    for i in range(len(games)):
        if games[i]["id"] == id:
            games.pop(i)
            break

    data = open('bd.json', 'w')
    json.dump(games, data, indent=4)
    data.close()

    return make_response(
        jsonify(
            message= "Game deleted",
            game= games
        )
    )

@games_bp.route('/games/<int:id>', methods=['PUT'])
def edit_game(id):
    data = open('bd.json')
    games = json.load(data)
    data.close()

    new_game_data = request.get_json()

    for i in range(len(games)):
        if games[i]["id"] == id:
            games[i]["id"] = new_game_data["id"]
            games[i]["name"] = new_game_data["name"]
            games[i]["year"] = new_game_data["year"]
            break
    
    data = open('bd.json', 'w')
    json.dump(games, data, indent=4)
    data.close()

    return make_response(
        jsonify(
            message= "Game edited",
            game= new_game_data
        )
    )