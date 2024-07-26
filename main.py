from flask import Flask
from blueprints.games.games import games_bp
from pymongo import MongoClient

app = Flask(__name__)
app.json.sort_keys = False

# Set up MongoDB client
mongo_client = MongoClient('mongodb://localhost:27017/')
app.config['MONGO_CLIENT'] = mongo_client
app.config['MONGO_DB'] = mongo_client['gamesData']

app.register_blueprint(games_bp)

if __name__ == '__main__':
    app.run(debug=True)