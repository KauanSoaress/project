from flask_security import UserMixin, RoleMixin
from main import db

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)

class User(db.Document, UserMixin):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    roles = db.ListField(db.ReferenceField(Role), default=[])