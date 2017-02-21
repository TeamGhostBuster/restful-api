from bson.objectid import ObjectId
from flask_mongoengine import DoesNotExist

from app.api.article.model import Article
from app.api.library.model import List
from app.api.user.model import User
from app.api.comment.model import Comment


def find_user(email):
    # Find the existed user by email
    try:
        user = User.objects.get(email__exact=email)

    except DoesNotExist:
        # The user does not exist
        return None

    return user


def create_user(email, first_name, last_name):
    # Create new user
    new_user = User(email=email, first_name=first_name, last_name=last_name).save()

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


def add_tag(article_id, tag):
    try:
        article = Article.objects.get(id=ObjectId(article_id))
    except DoesNotExist:
        return None

    # Add tag to article
    Article.objects(id=ObjectId(article_id)).update_one(push__tags=tag)
    article.reload()

    return article


def add_comment(user, article_id, comment, public=True):
    # Check if the article exists
    if find_article(article_id) is None:
        return None

    # Post comment
    new_comment = Comment(content=comment, article=article_id, public=public,
                          user=user).save()

    return new_comment

