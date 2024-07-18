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


def delete_or_edit_game(id):
    if request.method == 'DELETE':
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
    elif request.method == 'PUT':
        data = open('bd.json')
        games = json.load(data)
        data.close()

        new_game_data = request.get_json()

        for i in range(len(games)):
            if games[i]["id"] == id:
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
