from app.api.user.model import User


def find_user(email):
    user = User.objects(email__exact=email)
    if User.objects(email__exact=email).count() == 0:
        return None
    return user


def create_user(email):
    user = User(email=email).save()
    return user

