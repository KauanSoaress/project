from flask import Flask
from blueprints.helloworld.helloworld import helloworld_bp
from blueprints.games.games import games_bp

app = Flask(__name__)
app.json.sort_keys = False
app.register_blueprint(helloworld_bp, url_prefix="/hello")
app.register_blueprint(games_bp)

if __name__ == '__main__':
    app.run(debug=True)