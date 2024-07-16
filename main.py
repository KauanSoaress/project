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

    new_game = request.get_json()

    games.append(new_game)

    json.dump(games, data)
    data.close()
    return make_response(
        jsonify(
            message= 'Game created', 
            game= jsonify(new_game)
        )
    )