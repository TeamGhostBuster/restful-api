from marshmallow import Schema, fields
from app.api.comment.model import Comment, CommentSchema

from app import db


class Article(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    url = db.URLField()
    tags = db.ListField(db.StringField())
    comments = db.ListField(db.ReferenceField(Comment))

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '{{id: {}, title: {}}}'.format(self.id, self.title)


class ArticleSchema(Schema):
    """
    JSON Serialization and Deserialization
    """
    id = fields.String()
    title = fields.Str()
    description = fields.Str()
    url = fields.Url()
    tags = fields.List(fields.Str())
    comments = fields.Nested(CommentSchema, many=True, only=('id', 'content', 'created_at', 'author'))

    class Meta:
        fields = ('id', 'title', 'description', 'url', 'tags', 'comments')
        ordered = True
