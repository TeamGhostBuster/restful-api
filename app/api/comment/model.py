import datetime

from app import db
from app.api.article.model import Article
from app.api.user.model import User


class Comment(db.Document):
    content = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    article_id = db.ReferenceField(Article)
    user_id = db.ReferenceField(User)
