# import sys
# print(sys.path)
# exit()


from app.api.list.model import List
from app.api.user.model import User
from app import db


class Library(db.Document):
    owner = db.ReferenceField(User, required=True)
    lists = db.ListField(db.ReferenceField(List))

    def __str__(self):
        return 'ID: {}'.format(self.id)
