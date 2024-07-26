from flask import jsonify, request, make_response, current_app
from utils.VerifyParameters import verify_name, verify_year, exists_id
import json

def get_games():
    db = current_app.config['MONGO_DB']
    games_collection = db['games']
    games = list(games_collection.find({}, {"_id": 0, "name": 1, "year": 1}))

    # Convertendo i _id para string no caso de precisar mostrá-lo
    # for game in games:
    #     game['_id'] = str(game['_id'])

    return make_response(
        jsonify(
            message= 'Games list', 
            games= games
        )
    )

def post_games():
    new_game = request.get_json()

    if not verify_name(new_game) or not verify_year(new_game):
        return make_response(
            jsonify(
                message= 'Register Error: Invalid name or year',
            ),
            400
        )

    db = current_app.config['MONGO_DB']
    games_collection = db['games']

    print(new_game)

    result = games_collection.insert_one(new_game)

    print(new_game)
    new_game_id = result.inserted_id

    new_game['_id'] = str(new_game_id)

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
