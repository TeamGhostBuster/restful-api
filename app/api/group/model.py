from marshmallow import Schema, fields

from app import db
from app.api.list.model import List, ListSchema
from app.api.user.model import User, UserSchema


class Group(db.Document):
    name = db.StringField(required=True)
    description = db.StringField()
    moderator = db.ReferenceField(User, required=True)
    lists = db.ListField(db.ReferenceField(List))
    members = db.ListField(db.ReferenceField(User))

    def __str__(self):
        return 'ID: {} Name: {}'.format(self.id, self.name)


class GroupSchema(Schema):
    """
    JSON Serialization and Deserialization
    """
    id = fields.String()
    name = fields.String()
    moderator = fields.Nested(UserSchema, only=('id', 'first_name', 'last_name'))
    members = fields.Nested(UserSchema, many=True, only=('id', 'first_name', 'last_name'))
    lists = fields.Nested(ListSchema, many=True, only=('id', 'name'))
    description = fields.String()

    class Meta:
        fields = ('id', 'name', 'description', 'moderator', 'members', 'lists')
        ordered = True
