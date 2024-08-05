from flask import Flask, redirect, request, url_for, flash
from blueprints.games.games import games_bp
from blueprints.authentication.authentication import auth_bp
from pymongo import MongoClient

app = Flask(__name__)
app.json.sort_keys = False

# Conexão com o Mongo
mongo_client = MongoClient('mongodb://localhost:27017/')
app.config['MONGO_CLIENT'] = mongo_client
app.config['MONGO_DB'] = mongo_client['gamesData']

app.register_blueprint(games_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)