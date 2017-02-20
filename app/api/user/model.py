from app import db
from app.api.list.model import List


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    lists = db.ListField(db.ReferenceField(List))

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'ID: {} Email: {}'.format(self.id, self.email)
