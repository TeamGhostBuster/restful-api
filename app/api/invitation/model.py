from app import db
from app.api.user.model import User, UserSchema
from app.api.group.model import Group, GroupSchema

from marshmallow import Schema, fields


class Invitation(db.Document):
    inviter = db.ReferenceField(User, required=True)
    invitee = db.ReferenceField(User, required=True)
    group = db.ReferenceField(Group, required=True)


class InvitationSchema(Schema):
    id = fields.String()
    inviter = fields.Nested(UserSchema, only=('first_name', 'last_name', 'email'))
    invitee = fields.Nested(UserSchema, only=('first_name', 'last_name', 'email'))
    group = fields.Nested(GroupSchema, only=('id', 'name'))
