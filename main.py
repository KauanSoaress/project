import os
from flask import Flask
from blueprints.auth.auth import auth_bp
from blueprints.games.games import games_bp
from pymongo import MongoClient
from models.role_model import Role
from models.user_model import User
from mongoengine import connect
from flask_security import Security, MongoEngineUserDatastore, hash_password
import flask_wtf

# Create app
app = Flask(__name__)
app.json.sort_keys = False
app.config['DEBUG'] = True

# Have cookie sent
app.config["SECURITY_CSRF_COOKIE_NAME"] = "XSRF-TOKEN"

# Don't have csrf tokens expire (they are invalid after logout)
app.config["WTF_CSRF_TIME_LIMIT"] = None

# Enable CSRF protection
flask_wtf.CSRFProtect(app)

# Generate a nice key using secrets.token_urlsafe()
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
# Generate a good salt for password hashing using: secrets.SystemRandom().getrandbits(128)
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
# Don't worry if email has findable domain
app.config["SECURITY_EMAIL_VALIDATOR_ARGS"] = {"check_deliverability": False}
app.config["SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS"] = True
app.config["SECURITY_CSRF_PROTECT_MECHANISMS"] = ("basic", "session")
app.config["WTF_CSRF_CHECK_DEFAULT"] = False

# Conexão com o Mongo
mongo_client = MongoClient('mongodb://localhost:27017/')
app.config['MONGO_CLIENT'] = mongo_client
app.config['MONGO_DB'] = mongo_client['gamesData']

# Registrando blueprints
app.register_blueprint(games_bp)
app.register_blueprint(auth_bp)

# Create database connection object
db_name = "mydatabase"
db = connect(host="mongodb://localhost", port=27017)

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# one time setup
with app.app_context():
    # Create a user and role to test with
    security.datastore.find_or_create_role(
        name="user", permissions={"user-read", "user-write"}
    )
    if not security.datastore.find_user(email="test@me.com"):
        security.datastore.create_user(email="test@me.com",
        password=hash_password("password"), roles=["user"])

if __name__ == '__main__':
    app.run(debug=True)