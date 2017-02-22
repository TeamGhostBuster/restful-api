from app import db
from app.api.list.model import List
from app.api.user.model import User


class Group(db.Document):
    name = db.StringField(required=True)
    moderator = db.ReferenceField(User)
    lists = db.ListField(db.ReferenceField(List))
