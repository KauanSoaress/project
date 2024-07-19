from flask import jsonify, request, make_response
from .VerifyParameters import verify_name_and_year, exists_id
import json

def get_or_post_games():
    if request.method == 'GET':
        data = open('bd.json')
        games = json.load(data)
        data.close()
        
        if len(games) == 0:
            return make_response(
                jsonify(
                    message= 'Games list is empty',
                ),
                204
            )

        return make_response(
            jsonify(
                message= 'Games list', 
                game= games
            )
        )
    elif request.method == 'POST':
        with open('bd.json', 'r+') as data:
            games = json.load(data)

            new_game = request.get_json()

            if not verify_name_and_year(new_game):
                return make_response(
                    jsonify(
                        message= 'Register Error: Invalid name or year',
                    ),
                    422
                )
        
            position_to_insert = str(len(games) + 1)

            games[position_to_insert] = new_game

            data.seek(0)

            json.dump(games, data, indent=4)

            data.truncate()

        return make_response(
            jsonify(
                message= 'Game created', 
                game= new_game
            )
        )

def get_game_by_name(name): 
    data = open('bd.json')
    games = json.load(data)
    data.close()

    for index in games:
        if games[index]['name'] == name:
            return make_response (
                jsonify (
                    message= "Game found",
                    game= {
                        "name": games[index]['name'],
                        "year": games[index]['year']
                    }
                )
            )
        
    return make_response (
        jsonify (
            message= "Game not found"
        )
    )

def delete_or_edit_game(id):
    if request.method == 'DELETE':
        with open('bd.json', 'r+') as data:
            games = json.load(data)

            if not exists_id(id, games):
                return make_response(
                    jsonify(
                        message= 'Register Error: Invalid id',
                    ),
                    422
                )

            games.pop(id)

            data.seek(0)

            json.dump(games, data, indent=4)

            data.truncate()

        return make_response(
            jsonify(
                message= "Game deleted",
                game= games
            )
        )
    elif request.method == 'PUT':
        with open('bd.json', 'r+') as data:
            games = json.load(data)

            new_game_data = request.get_json()

            if not exists_id(id, games):
                return make_response(
                    jsonify(
                        message= 'Register Error: Invalid id',
                    ),
                    422
                )

            if not verify_name_and_year(new_game_data):
                return make_response(
                    jsonify(
                        message= 'Register Error: Invalid name or year',
                    ),
                    422
                )

            games[id]["name"] = new_game_data["name"]
            games[id]["year"] = new_game_data["year"]
            
            data.seek(0)

            json.dump(games, data, indent=4)

            data.truncate()

        return make_response(
            jsonify(
                message= "Game edited",
                game= new_game_data
            )
        )
