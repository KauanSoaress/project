from flask import jsonify, request, make_response
from utils.VerifyParameters import verify_name, verify_year, exists_id
import json

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

def post_games():
    with open('bd.json', 'r+') as data:
        games = json.load(data)

        new_game = request.get_json()

        if not verify_name(new_game) or not verify_year(new_game):
            return make_response(
                jsonify(
                    message= 'Register Error: Invalid name or year',
                ),
                400
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

def delete_game(id):
    with open('bd.json', 'r+') as data:
        games = json.load(data)

        if not exists_id(id, games):
            return make_response(
                jsonify(
                    message= 'Delete Error: Invalid id',
                ),
                400
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

def edit_game(id):
    with open('bd.json', 'r+') as data:
        games = json.load(data)

        new_game_data = request.get_json()

        if not exists_id(id, games):
            return make_response(
                jsonify(
                    message= 'Edit Error: Invalid id',
                ),
                400
            )

        if not verify_name(new_game_data) or not verify_year(new_game_data):
            return make_response(
                jsonify(
                    message= 'Register Error: Invalid name or year',
                ),
                400
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
