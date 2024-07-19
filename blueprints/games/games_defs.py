from flask import jsonify, request, make_response
import json

def get_or_post_games():
    if request.method == 'GET':
        data = open('bd.json')
        games = json.load(data)
        data.close()
        
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

def delete_or_edit_game(id):
    if request.method == 'DELETE':
        with open('bd.json', 'r+') as data:
            games = json.load(data)

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
