from flask import Flask
from blueprints.user.user import user_bp
from blueprints.games.games import games_bp
from pymongo import MongoClient

# Create app
app = Flask(__name__)
app.json.sort_keys = False
app.config['DEBUG'] = True

# Conexão com o Mongo
mongo_client = MongoClient('mongodb://localhost:27017/')
app.config['MONGO_CLIENT'] = mongo_client
app.config['MONGO_DB'] = mongo_client['gamesData']

# Registrando blueprints
app.register_blueprint(games_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
