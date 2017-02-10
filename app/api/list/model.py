from app import db
from app.api.article.model import Article


class List(db.Document):
    name = db.StringField()
    articles = db.ListField(db.ReferenceField(Article))

    def __str__(self):
        return 'ID: {}'.format(self.id)
