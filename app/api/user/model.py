from mongoengine import *
from app import db


class User(db.Document):
    email = EmailField(required=True)
