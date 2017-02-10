from app.api.user.model import User
from app.api.article.model import Article
from app.api.library.model import List


def find_user(email):
    user = User.objects(email__exact=email)
    if User.objects(email__exact=email).count() == 0:
        return None
    return user


def create_user(email):
    # Create new user
    new_user = User(email=email).save()

    return new_user


def find_list(list_id):
    # Find user's list
    user_list = List.objects(id=list_id)

    # Check if exists
    if List.objects(id__exact=list_id).count() == 0:
        return False

    return user_list


def create_list(list_name):
    # Create new list
    new_list = List(name=list_name).save()

    return new_list


def create_article(title, list_id, tags=None):
    # Create new article
    new_article = Article(title=title).save()

    # Add article the user's list
    List.objects(id=list_id).update_one(push__articles=new_article).save()

    return new_article



