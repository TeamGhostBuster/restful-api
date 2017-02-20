from app import db


class Article(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    tags = db.ListField(db.StringField)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'ID: {} Title: {}'.format(self.id, self.title)
