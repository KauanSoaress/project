from flask import jsonify, request, make_response, current_app
from utils.verify.verify_parameters import verify_name, verify_year, verify_id
from bson import ObjectId


def get_games():
    db = current_app.config['MONGO_DB']
    games_collection = db['games']

    games = list(games_collection.find({}, {"_id": 0, "name": 1, "year": 1}))

    return make_response(
        jsonify(
            message='Games list',
            games=games
        )
    )


def post_games():
    new_game = request.get_json()

    if not verify_id(new_game['user_id']):
        return make_response(
            jsonify(
                message='Error: Invalid user id',
            ),
            400
        )

    if not verify_name(new_game) or not verify_year(new_game):
        return make_response(
                jsonify(
                    message='Error: Invalid name or year',
                ),
                400
            )

    db = current_app.config['MONGO_DB']
    games_collection = db['games']

    result = games_collection.insert_one(new_game)

    # Convertendo o id para string para mostrá-lo
    new_game_id = result.inserted_id
    new_game['_id'] = str(new_game_id)

    return make_response(
        jsonify(
            message='Game created',
            game=new_game
        )
    )


def get_game_by_name(name):
    db = current_app.config['MONGO_DB']
    games_collection = db['games']

    game = games_collection.find_one({"name": name}, {"_id": 0, "name": 1, "year": 1, "user_id": 1})

    # Convertendo i _id para string no caso de precisar mostrá-lo
    # game['_id'] = str(game['_id'])

    if game:
        return make_response(
                jsonify(
                    message="Game found",
                    game=game
                )
            )

    return make_response(
        jsonify(
            message="Game not found"
        )
    )


def get_games_by_user_id(user_id):
    db = current_app.config['MONGO_DB']
    games_collection = db['games']

    games = list(games_collection.find({"user_id": user_id}, {"_id": 0, "name": 1, "year": 1}))

    return make_response(
        jsonify(
            message='Games list',
            games=games
        )
    )


def delete_game(id):
    if not verify_id(id):
        return make_response(
            jsonify(
                message='Error: Invalid id',
            ),
            400
        )

    db = current_app.config['MONGO_DB']
    games_collection = db['games']

    delete_status = games_collection.delete_one({"_id": ObjectId(id)})

    if delete_status.deleted_count == 0:
        return make_response(
            jsonify(
                message='Edit Error: Game not found',
            )
        )

    return make_response(
        jsonify(
            message="Game deleted",
        )
    )


def delete_games_by_user_id(user_id):
    db = current_app.config['MONGO_DB']
    games_collection = db['games']

    games_collection.delete_many({"user_id": user_id})


def edit_game(id):
    data = request.get_json()

    if not verify_id(id):
        return make_response(
            jsonify(
                message='Error: Invalid id',
            ),
            400
        )

    if not verify_name(data) or not verify_year(data):
        return make_response(
            jsonify(
                message='Error: Invalid name or year',
            ),
            400
        )

    db = current_app.config['MONGO_DB']
    games_collection = db['games']

    edit_status = games_collection.update_one({"_id": ObjectId(id)}, {"$set": data})

    if edit_status.modified_count == 0:
        return make_response(
            jsonify(
                message='Edit Error: Game not found',
            )
        )

    return make_response(
        jsonify(
            message="Game edited"
        )
    )
