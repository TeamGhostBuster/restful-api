import mongoengine

from app import db
from app.api.article.model import Article, ArticleSchema
from marshmallow import Schema, fields


class List(db.Document):
    name = db.StringField(required=True)
    articles = db.ListField(db.ReferenceField(Article, reverse_delete_rule=mongoengine.PULL))
    archived = db.BooleanField(default=False)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'id: {}, name:{}, articles: {}'.format(str(self.id), self.name, self.articles)


class ListSchema(Schema):
    """
    JSON Serialization and Deserialization
    """
    id = fields.String()
    name = fields.String()
    articles = fields.Nested(ArticleSchema, many=True, only=('id', 'title', 'creator'))
    archived = fields.Boolean()

    class Meta:
        fields = ('id', 'name', 'articles', 'archived')
        ordered = True
