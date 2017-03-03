import datetime

from marshmallow import Schema, fields

from app import db


class Comment(db.Document):
    """
    MongoDB ORM model
    """
    content = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    author = db.EmailField()
    public = db.BooleanField(default=True)


class CommentSchema(Schema):
    """
    JSON Serialization and Deserialization
    """
    id = fields.String()
    content = fields.Str()
    created_at = fields.DateTime()
    author = fields.Str()
    public = fields.Boolean()

    class Meta:
        fields = ('id', 'content', 'created_at', 'author', 'public')
        order = True
