from flask import jsonify, request, make_response, current_app
from bson import ObjectId
from utils.verify.verify_parameters import verify_name, verify_age, verify_id
from utils.games_utils.games_defs import delete_games_by_user_id


def get_user():
    db = current_app.config['MONGO_DB']
    users_collection = db['users']

    user = list(users_collection.find({}, {"_id": 0, "name": 1, "age": 1}))

    return make_response(
        jsonify(
            message='User list',
            user=user
        )
    )


def get_user_by_id(id):
    if not verify_id(id):
        return make_response(
            jsonify(
                message='Error: Invalid id',
            ),
            400
        )

    db = current_app.config['MONGO_DB']
    users_collection = db['users']

    user = users_collection.find_one({"_id": ObjectId(id)}, {"_id": 0, "name": 1, "age": 1})

    if user:
        return make_response(
            jsonify(
                message='User found',
                user=user
            )
        )

    return make_response(
        jsonify(
            message='User not found'
        )
    )


def post_user():
    new_user = request.get_json()

    if not verify_name(new_user) or not verify_age(new_user):
        return make_response(
                jsonify(
                    message='Error: Invalid name or age',
                ),
                400
            )

    db = current_app.config['MONGO_DB']
    users_collection = db['users']

    result = users_collection.insert_one(new_user)

    # Convertendo o id para string para mostrá-lo
    new_user_id = result.inserted_id
    new_user['_id'] = str(new_user_id)

    return make_response(
        jsonify(
            message='User created',
            game=new_user
        )
    )


def delete_user(id):
    if not verify_id(id):
        return make_response(
            jsonify(
                message='Error: Invalid id',
            ),
            400
        )

    db = current_app.config['MONGO_DB']
    users_collection = db['users']

    result = users_collection.delete_one({"_id": ObjectId(id)})
    delete_games_by_user_id(id)

    if result.deleted_count == 0:
        return make_response(
            jsonify(
                message='Error: User not found',
            ),
            404
        )

    return make_response(
        jsonify(
            message='User deleted',
        )
    )


def edit_user(id):
    if not verify_id(id):
        return make_response(
            jsonify(
                message='Error: Invalid id',
            ),
            400
        )

    updated_user = request.get_json()

    if not verify_name(updated_user) or not verify_age(updated_user):
        return make_response(
                jsonify(
                    message='Error: Invalid name or age',
                ),
                400
            )

    db = current_app.config['MONGO_DB']
    users_collection = db['users']

    result = users_collection.update_one(
        ({"_id": ObjectId(id)}),
        {"$set": updated_user}
    )

    if result.matched_count == 0:
        return make_response(
            jsonify(
                message='Error: User not found',
            ),
            404
        )

    return make_response(
        jsonify(
            message='User updated'
        )
    )
