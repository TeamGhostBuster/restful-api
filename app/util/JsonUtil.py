from app.api.article.model import Article, ArticleSchema
from app.api.comment.model import Comment, CommentSchema
from app.api.list.model import List, ListSchema
from app.api.user.model import User, UserSchema
from app.api.group.model import Group, GroupSchema
from app.api.vote.model import Vote, VoteSchema


def serialize(obj, only=tuple(), exclude=tuple()):
    """
    Python object serializer
    :param obj: The object to parse into json string
    :return: A dictionary
    """

    # An Article object
    if isinstance(obj, Article):
        schema = ArticleSchema(only=only, exclude=exclude)
        return dict(schema.dump(obj).data)

    elif isinstance(obj, Comment):
        schema = CommentSchema(only=only, exclude=exclude)
        return schema.dump(obj).data

    elif isinstance(obj, List):
        schema = ListSchema(only=only, exclude=exclude)
        return dict(schema.dump(obj).data)

    elif isinstance(obj, User):
        schema = UserSchema(only=only, exclude=exclude)
        return dict(schema.dump(obj).data)

    elif isinstance(obj, Group):
        schema = GroupSchema(only=only, exclude=exclude)
        return dict(schema.dump(obj).data)

    elif isinstance(obj, Vote):
        schema = VoteSchema()
        return dict(schema.dump(obj).data)
