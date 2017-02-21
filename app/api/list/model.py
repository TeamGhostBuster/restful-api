from marshmallow import Schema, fields

from app import db
from app.api.article.model import Article, ArticleSchema


class List(db.Document):
    name = db.StringField(required=True)
    articles = db.ListField(db.ReferenceField(Article))

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

    class Meta:
        fields = ('id', 'name', 'articles')
        ordered = True
