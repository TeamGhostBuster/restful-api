from mongoengine import *
from app import db


class User(db.Document):
    email = EmailField(required=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'ID: {} Email: {}'.format(self.id, self.email)
