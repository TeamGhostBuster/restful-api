import datetime
from marshmallow import Schema, fields

from app import db
from app.api.article.model import Article
from app.api.user.model import User


class Comment(db.Document):
    """
    MongoDB ORM model
    """
    content = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    article = db.ReferenceField(Article)
    user = db.ReferenceField(User)
    public = db.BooleanField()


class CommentSchema(Schema):
    """
    JSON Serialization and Deserialization
    """
    id = fields.String()
    content = fields.Str()
    created_at = fields.DateTime()
    user = fields.String()
    article = fields.String()
    public = fields.Boolean()

    class Meta:
        fields = ('id', 'content', 'created_at', 'user', 'article', 'public')
        order = True
