from app.api.article.model import Article, ArticleSchema
from app.api.comment.model import Comment, CommentSchema


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
        return dict(schema.dump(obj).data)
