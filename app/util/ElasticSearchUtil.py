from app import es
from app.util import JsonUtil


def save_to_es(article):
    """
    Save article to elasticsearch
    :param article: The article to save.
    :return: None
    """
    doc = JsonUtil.serialize(article)
    es.index(index='raspberry', doc_type='article', id=article.id, body=doc)

