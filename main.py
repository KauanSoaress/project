from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)
app.json.sort_keys = False

# content_type do tipo application/json

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/games', methods=['GET'])
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

@app.route('/games/<string:name>', methods=['GET'])
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
        
@app.route('/games', methods=['POST'])
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

@app.route('/games/<int:id>', methods=['DELETE'])
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

@app.route('/games/<int:id>', methods=['PUT'])
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