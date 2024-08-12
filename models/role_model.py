from mongoengine import Document, StringField, ListField
from flask_security import RoleMixin


class Role(Document, RoleMixin):
    name = StringField(max_length=80, unique=True)
    permissions = ListField(required=False)
