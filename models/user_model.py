from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField
from flask_security import UserMixin
from models.role_model import Role
import uuid

class User(Document, UserMixin):
    email = StringField(max_length=255, unique=True)
    password = StringField(max_length=255)
    fs_uniquifier = StringField(max_length=64, unique=True, default=lambda: str(uuid.uuid4()))
    active = BooleanField(default=True)
    roles = ListField(ReferenceField(Role), default=[])