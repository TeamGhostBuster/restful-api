from copy import deepcopy

from bson.objectid import ObjectId
from flask_mongoengine import DoesNotExist
from mongoengine.queryset.visitor import Q

from app.api.article.model import Article
from app.api.comment.model import Comment
from app.api.group.model import Group
from app.api.list.model import List
from app.api.user.model import User
from app.api.vote.model import Vote

from app.exception.UserHasVoted import UserHasVoted


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
        # Find reading list
        user_list = List.objects.get(id=ObjectId(list_id))
    except Exception as e:
        return type(e).__name__

    return user_list


def archive_list(user, list_id):
    try:
        # Get the list
        archived_list = List.objects.get(id=ObjectId(list_id))
        User.objects.get(id=user.id, lists=archived_list)
    except DoesNotExist as e:
        return None

    # Mark it as archived
    List.objects(id=archived_list.id).update_one(archived=True)

    user.reload()

    return user


def retrieve_list(user, list_id):
    try:
        retrieved_list = List.objects.get(id=ObjectId(list_id))
        User.objects.get(id=user.id, lists=retrieved_list)
    except DoesNotExist:
        return None

    # Mark it as not archived
    List.objects(id=retrieved_list.id).update_one(archived=False)

    user.reload()

    return user


def archive_group_list(group_id, list_id):
    try:
        # Check if list exists
        archived_list = List.objects.get(id=ObjectId(list_id))
        # Check if the list belongs to the group
        group = Group.objects.get(id=ObjectId(group_id), lists=archived_list)
    except DoesNotExist:
        return None

    List.objects(id=archived_list.id).update_one(archived=True)

    return group


def retrieve_group_list(group_id, list_id):
    try:
        # Check if list exists
        retrieved_list = List.objects.get(id=ObjectId(list_id))
        # Check if the list belongs to the group
        group = Group.objects.get(id=ObjectId(group_id), lists=retrieved_list)
    except DoesNotExist:
        return None

    List.objects(id=retrieved_list.id).update_one(archived=False)

    return group


# def get_user_all_lists(user):
#     # user = User.objects.get(id=user.id, lists__)
#     pipeline = [
#         {'$match': {'email': 'michaellam.lzc@gmail.com'}},
#         {'$unwind': '$lists'},
#         {'$lookup': {
#             'from': 'list',
#             'localField': 'lists',
#             'foreignField': '_id',
#             'as': 'listObj'
#         }},
#         {'$unwind': '$listObj'},
#         {'$match': {'listObj.archived': {'$ne': 'true'}}},
#         {'$group': {'_id': '$_id',
#                     'email': {'$first': '$email'},
#                     'last_name': {'$first': '$last_name'},
#                     'first_name': {'$first': 'first_name'},
#                     'lists': {'$push': '$lists'}}}
#     ]
#     pass


def create_list(list_name, user):
    # Create new list
    new_list = List(name=list_name).save()

    # Append list reference to the user's lists list
    User.objects(id=user.id).update_one(push__lists=new_list)

    return new_list


def create_article(data, list_id):
    try:
        # Check if list exists
        List.objects.get(id=ObjectId(list_id))
        # Create new article
        new_article = Article(**data).save()
    except Exception as e:
        return type(e).__name__

    # Append article reference to the user's article lists
    List.objects(id=list_id).update_one(push__articles=new_article)

    return new_article


def update_article(data, article_id):
    try:
        # Check if the article exists
        article = Article.objects.get(id=ObjectId(article_id))
        # Update article
        Article.objects(id=ObjectId(article_id)).update_one(**data)
    except Exception as e:
        return type(e).__name__
    # Article.objects(id=ObjectId(article_id)).update_one(**data)
    article.reload()
    return article


def create_article_in_group(data, list_id, group_id):
    try:
        # Check if the list exist
        the_list = List.objects.get(id=ObjectId(list_id))
        # Check if the list belongs to the group
        the_group = Group.objects.get(id=ObjectId(group_id), lists=the_list)
    except DoesNotExist:
        return None

    # create new article
    new_article = create_article(data, list_id)

    return new_article


def find_article(article_id):
    # Find the article
    try:
        article = Article.objects.get(id=ObjectId(article_id))

    except DoesNotExist:
        return None

    return article


def add_article_to_list(list_id, article_id):
    # Find the article
    try:
        article = find_article(article_id)
    except DoesNotExist:
        return None

    # Find the list
    try:
        reading_list = find_list(list_id)
    except DoesNotExist:
        return None

    # Add the article to the list
    List.objects(id=ObjectId(list_id)).update_one(push__articles=article)
    reading_list.reload()

    return reading_list


def add_tag(article_id, tag):
    try:
        article = Article.objects.get(id=ObjectId(article_id))
    except DoesNotExist:
        return None

    # Add tag to article
    Article.objects(id=article.id).update_one(push__tags=tag)
    article.reload()

    return article


def delete_article(user, list_id, article_id):
    # Retrieve the articled and list to be deleted
    try:
        the_list = List.objects.get(id=ObjectId(list_id))
        the_article = Article.objects.get(id=ObjectId(article_id))
    except DoesNotExist:
        return None

    # Check if user has permission to the list
    if the_list not in user.lists:
        return None

    # Check if the article exists in the list
    if the_article not in the_list.articles:
        return None

    # Remove the article from the list
    List.objects(id=the_list.id).update_one(pull__articles=the_article)

    the_list.reload()

    return the_list


def add_comment(user, article_id, comment, public=True):
    try:
        # Check if article exists
        article = Article.objects.get(id=ObjectId(article_id))
        # Post comment
        new_comment = Comment(content=comment, public=public, author=user.email).save()
        # Add reference to the article
        Article.objects(id=article.id).update_one(push__comments=new_comment)

    except Exception as e:
        return type(e).__name__

    return new_comment


def create_group(group_name, moderator, members=None, description=None):
    # Create group
    new_group = Group(name=group_name, moderator=moderator, description=description).save()

    # Add moderator to members
    Group.objects(id=new_group.id).update_one(push__members=moderator)

    # Add members if not null
    if members is not None:
        for id in members:
            try:
                member = User.objects.get(id=ObjectId(id))
                Group.objects(id=new_group.id).update_one(push__members=member)
            except DoesNotExist:
                return None

    new_group.reload()
    return new_group


def find_group(group_id):
    try:
        # Find group
        reading_group = Group.objects.get(id=ObjectId(group_id))
    except DoesNotExist:
        return None
    return reading_group


def add_group_member(group_id, member_id):
    # Find the group
    try:
        reading_group = find_group(group_id)
    except DoesNotExist:
        return None

    # Check that new member exists
    try:
        new_member = User.objects.get(id=ObjectId(member_id))
    except DoesNotExist:
        return None

    # Add group member
    Group.objects(id=ObjectId(group_id)).update_one(push__members=new_member)
    reading_group.reload()

    return reading_group


def create_group_list(user, list_name, group_id):
    # Check if user has permission
    # Create list
    new_list = List(name=list_name).save()

    # Append list reference to the group's list of lists
    try:
        Group.objects(id=ObjectId(group_id)).update_one(push__lists=new_list)
    except DoesNotExist:
        return None
    return new_list


def get_user_groups(user):
    groups = Group.objects(members=user)

    if Group.objects(members=user).count() == 0:
        return None

    return groups


def get_group_lists(user, group_id):
    try:
        # Get group
        group = Group.objects.get(id=ObjectId(group_id), members=user)
    except DoesNotExist:
        return None

    return group


def check_user_in_group(user, group_id):
    try:
        # Check if user belongs to the group
        Group.objects.get(id=ObjectId(group_id), members=user)
    except DoesNotExist:
        return None

    return 0


def share_list_to_group(user, list_id, group_id):
    try:
        # Check if the list exist
        the_list = List.objects.get(id=ObjectId(list_id))
        # Check if user has permission to the list or not
        User.objects.get(id=user.id, lists=the_list)
    except DoesNotExist:
        return None

    duplicate_list = deepcopy(the_list)
    duplicate_list.id = None
    duplicate_list.save()
    Group.objects(id=ObjectId(group_id)).update_one(push__lists=duplicate_list)
    return duplicate_list


def check_vote_exist(list, article):
    try:
        # Try to retrieve the vote
        vote = Vote.objects.get(list=list, article=article)
    except DoesNotExist:
        # If it does not exist, create a new one instead
        vote = Vote(list=list, article=article).save()

    return vote


def check_user_has_upvoted(user, vote):
    try:
        # Check if user has upvoted or not
        Vote.objects.get(Q(id=vote.id) & Q(upvoter_list=user))
    except DoesNotExist:
        # User have not upvote
        return False

    return True


def check_user_has_downvoted(user, vote):
    try:
        # Check if user has downvoted or not
        vote = Vote.objects.get(Q(id=vote.id) & Q(downvoter_list=user))
    except DoesNotExist:
        # User have not downvote
        return False

    return True


def upvote_article(user, group_id, list_id, article_id):
    try:
        # Resources check
        article = Article.objects.get(id=ObjectId(article_id))
        group = Group.objects.get(id=ObjectId(group_id), lists=ObjectId(list_id), members=user)
        list = List.objects.get(id=ObjectId(list_id), articles=article)

        # Create new vote
        vote = check_vote_exist(list, article)
        if check_user_has_upvoted(user, vote):
            raise UserHasVoted('User cannot vote twice.')

        # Upvote the article
        Vote.objects(id=vote.id).update_one(push__upvoter_list=user, pull__downvoter_list=user, vote_count=vote.vote_count+1)
    except Exception as e:
        return type(e).__name__

    vote.reload()
    return vote


def downvote_article(user, group_id, list_id, article_id):
    try:
        # Resources check
        article = Article.objects.get(id=ObjectId(article_id))
        group = Group.objects.get(id=ObjectId(group_id), lists=ObjectId(list_id), members=user)
        list = List.objects.get(id=ObjectId(list_id), articles=article)

        # Create new vote
        vote = check_vote_exist(list, article)
        if check_user_has_downvoted(user, vote):
            raise UserHasVoted('User cannot vote twice.')

        # Downvote the article
        Vote.objects(id=vote.id).update_one(push__downvoter_list=user, pull__upvoter_list=user, vote_count=vote.vote_count-1)
    except Exception as e:
        return type(e).__name__

    vote.reload()
    return vote


def get_vote_count(list_id, article_id):
    try:
        list = List.objects.get(id=ObjectId(list_id))
        article = Article.objects.get(id=ObjectId(article_id))
        vote = Vote.objects.get(Q(list=list) & Q(article=article))
    except Exception as e:
        return type(e).__name__

    return vote.vote_count


def add_vote_count(group_list):
    for i, article in enumerate(group_list['articles']):
        group_list['articles'][i]['vote_count'] = get_vote_count(group_list['id'], article['id'])

    return group_list
