from app import db
from marshmallow import Schema, fields
from app.api.article.model import Article, ArticleSchema
from app.api.list.model import List, ListSchema
from app.api.user.model import User, UserSchema


class Vote(db.Document):
    article = db.ReferenceField(Article)
    list = db.ReferenceField(List)
    vote_count = db.IntField(default=0)
    voter_list = db.ListField(db.ReferenceField(User))

    def __str__(self):
        return 'id: {}, article {}'.format(str(self.id), self.article)


class VoteSchema(Schema):
    """
    JSON Serialization and Deserialization
    """
    id = fields.String()
    article = fields.Nested(ArticleSchema, only=('id', 'title'))
    list = fields.Nested(ListSchema, only=('id', 'name'))
    vote_count = fields.Int()
    voter_list = fields.Nested(UserSchema, many=True, only='id')

    class Meta:
        fields = ('id', 'vote_count', 'article', 'list')
        ordered = True
