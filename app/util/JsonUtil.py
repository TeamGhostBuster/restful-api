from app.api.article.model import Article, ArticleSchema


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
