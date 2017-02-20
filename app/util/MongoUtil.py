from flask_mongoengine import DoesNotExist
from bson.objectid import ObjectId

from app.api.article.model import Article
from app.api.library.model import List
from app.api.user.model import User


def find_user(email):
    # Find the existed user by email
    try:
        user = User.objects.get(email__exact=email)

    except DoesNotExist:
        # The user does not exist
        return None

    return user


def create_user(email):
    # Create new user
    new_user = User(email=email).save()

    return new_user


def find_list(list_id):
    try:
        # Find user's list
        user_list = List.objects.get(id=ObjectId(list_id))
    except DoesNotExist:
        pass

    return user_list


def get_article_from_list(list):
    articles = list.articles

    for i in articles:
        print(i.title)


def create_list(list_name, user):
    # Create new list
    new_list = List(name=list_name).save()

    # Append list reference to the user's lists list
    User.objects(id=user.id).update_one(push__lists=new_list)

    return new_list


def create_article(title, list_id, description=None, url=None, tags=None):
    # Check if list exists
    if List.objects(id=ObjectId(list_id)).count() == 0:
        return None

    # Create new article
    new_article = Article(title=title, description=description, url=url, tags=tags).save()

    # Append article reference to the user's article lists
    List.objects(id=list_id).update_one(push__articles=new_article)

    return new_article


def find_article(article_id):
    # Find the article
    try:
        article = Article.objects.get(id=ObjectId(article_id))

    except DoesNotExist:
        return None

    return article
