from marshmallow import Schema, fields

from app import db
from app.api.article.model import Article, ArticleSchema


class List(db.Document):
    name = db.StringField(required=True)
    articles = db.ListField(db.ReferenceField(Article))
    archived = db.BooleanField(default=False)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'id: {}, name:{}'.format(str(self.id), self.name)


class ListSchema(Schema):
    """
    JSON Serialization and Deserialization
    """
    id = fields.String()
    name = fields.String()
    articles = fields.Nested(ArticleSchema, many=True, only=('id', 'title'))
    archived = fields.Boolean()

    class Meta:
        fields = ('id', 'name', 'articles', 'archived')
        ordered = True
