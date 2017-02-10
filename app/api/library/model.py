from app import db
from app.api.list.model import List


class Library(db.Document):
    lists = db.ListField(db.ReferenceField(List))

    def __str__(self):
        return 'ID: {}'.format(self.id)
