from app import db
from app.api.list.model import List


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    lists = db.ListField(db.ReferenceField(List))
    first_name = db.StringField()
    last_name = db.StringField()

    def __repr__(self):
        return 'ID: {} Email: {}'.format(self.id, self.email)

    def __str__(self):
        return '{{id:{}, first_name:{}, last_name:{}}}'.format(str(self.id), self.first_name, self.last_name)
