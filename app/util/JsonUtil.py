from app.api.article.model import Article, ArticleSchema
from app.api.comment.model import Comment, CommentSchema
from app.api.list.model import List, ListSchema
from app.api.user.model import User, UserSchema
from app.api.group.model import Group, GroupSchema


def serialize(obj):
    """
    Python object serializer
    :param obj: The object to parse into json string
    :return: A dictionary
    """

    # An Article object
    if isinstance(obj, Article):
        schema = ArticleSchema()
        return dict(schema.dump(obj).data)

    elif isinstance(obj, Comment):
        schema = CommentSchema()
        return schema.dump(obj).data

    elif isinstance(obj, List):
        schema = ListSchema()
        return dict(schema.dump(obj).data)

    elif isinstance(obj, User):
        schema = UserSchema()
        return schema.dump(obj).data

    elif isinstance(obj, Group):
        schema = GroupSchema()
        return dict(schema.dump(obj).data)
