from mongoengine import *
from app import db


class User(db.Document):
    id = ObjectIdField(required=True)
    email = EmailField(required=True)
