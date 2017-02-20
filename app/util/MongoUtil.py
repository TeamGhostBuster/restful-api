from app.api.user.model import User
from app.api.article.model import Article
from app.api.library.model import List
from bson.objectid import ObjectId
from flask_mongoengine import DoesNotExist


def find_user(email):
    try:
        # Find the existed user by email
        user = User.objects.get(email__exact=email)
    except DoesNotExist:
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


def create_article(title, list_id, tags=None):
    # Create new article
    new_article = Article(title=title).save()

    # Append article reference to the user's article lists
    List.objects(id=list_id).update_one(push__articles=new_article, upsert=True)

    return new_article
