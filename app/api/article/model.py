from marshmallow import Schema, fields
from app.api.comment.model import Comment, CommentSchema

from app import db


class Article(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    url = db.URLField()
    tags = db.ListField(db.StringField())
    comments = db.ListField(db.ReferenceField(Comment))
    # Src: http://stackoverflow.com/a/24859907
    # Author: http://stackoverflow.com/users/156427/ross
    creator = db.ReferenceField('User', required=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'id: {}, title: {}'.format(self.id, self.title)


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
    # Src: https://github.com/marshmallow-code/marshmallow-sqlalchemy/issues/104
    # Author: https://github.com/xarg
    creator = fields.Nested('UserSchema', only=('id', 'email'))

    class Meta:
        fields = ('id', 'title', 'description', 'url', 'tags', 'comments', 'creator')
        ordered = True
