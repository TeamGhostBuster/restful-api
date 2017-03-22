from copy import deepcopy

from bson.objectid import ObjectId
from flask_mongoengine import DoesNotExist
from mongoengine.queryset.visitor import Q
from pymongo import UpdateOne

from app.api.article.model import Article
from app.api.comment.model import Comment
from app.api.group.model import Group
from app.api.list.model import List
from app.api.user.model import User
from app.api.vote.model import Vote
from app.api.invitation.model import Invitation

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


def bulk_retrieve_list(user, lists):
    try:
        bulk_list = List.objects.in_bulk([ObjectId(i) for i in lists]).values()
        bulk_ops = list()

        # URL: http://stackoverflow.com/questions/30943076/mongoengine-bulk-update-without-objects-update
        # Author: lucasdavid
        # Bulk update retrieve list
        for each in bulk_list:
            bulk_ops.append(UpdateOne({'_id': each.id}, {'$set': {'archived': False}}))

        # Execute
        collection = List._get_collection().bulk_write(bulk_ops, ordered=False)
    except Exception as e:
        return type(e).__name__


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


def rename_personal_list(user, list_id, new_name):
    try:
        # Rename the list
        the_list = List.objects.get(id=ObjectId(list_id))
        List.objects(id=the_list.id).update_one(name=new_name)

    except Exception as e:
        return type(e).__name__


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
        the_group = Group.objects.get(Q(id=ObjectId(group_id)) & Q(lists=the_list))
        # create new article
        new_article = create_article(data, list_id)
        # init the vote
        Vote(article=new_article, list=the_list).save()
    except Exception as e:
        return type(e).__name__

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
        # Check resource
        the_article = Article.objects.get(id=ObjectId(article_id))
        the_list = List.objects.get(Q(id=ObjectId(list_id)) & Q(articles=the_article))
        # Remove the article from the list
        List.objects(id=the_list.id).update_one(pull__articles=the_article)
    except Exception as e:
        return type(e).__name__

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
    member_buffer = list()
    if members:
        for email in members:
            try:
                user = User.objects.get(email=email)
                member_buffer.append(user)
            except Exception as e:
                return type(e).__name__
            finally:
                # Even if exception occurs, still be able to add a portion of user
                Group.objects(id=new_group.id).update_one(add_to_set__members=member_buffer)
        # Bulk update
        Group.objects(id=new_group.id).update_one(add_to_set__members=member_buffer)

    new_group.reload()
    return new_group


def find_group(group_id):
    try:
        # Find group
        reading_group = Group.objects.get(id=ObjectId(group_id))
    except DoesNotExist:
        return None
    return reading_group


def add_group_member(group_id, member_email):
    try:
        # Find the group and user
        reading_group = find_group(group_id)
        new_member = User.objects.get(email=member_email)
        # Add user to group
        Group.objects(id=ObjectId(group_id)).update_one(push__members=new_member)
    except Exception as e:
        return type(e).__name__

    # Add group member
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
        for group in group_id:
            duplicate_list = deepcopy(List.objects.get(id=ObjectId(list_id)))
            duplicate_list.id = None
            duplicate_list.save()
            # init the vote for each articles
            init_vote(duplicate_list)
            target_group = Group.objects.get(id=ObjectId(group))
            Group.objects(id=target_group.id).update_one(push__lists=duplicate_list)

    except Exception as e:
        return type(e).__name__


def init_vote(the_list):
    for article in the_list.articles:
        Vote(article=article, list=the_list).save()


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

        # Revoke vote
        if check_user_has_downvoted(user, vote):
            Vote.objects(id=vote.id).update_one(pull__downvoter_list=user, vote_count=vote.vote_count + 1)
        else:
            # Upvote article
            Vote.objects(id=vote.id).update_one(push__upvoter_list=user, vote_count=vote.vote_count+1)
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

        # User is just trying to take vote back
        if check_user_has_upvoted(user, vote):
            Vote.objects(id=vote.id).update_one(pull__upvoter_list=user, vote_count=vote.vote_count-1)
        else:
            # Downvote
            Vote.objects(id=vote.id).update_one(push__downvoter_list=user, vote_count=vote.vote_count-1)
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


def partition_user_list(user, old_list_id, new_list_name, articles):
    try:
        # Get list and create new list
        old_list = List.objects.get(id=ObjectId(old_list_id))
        new_list = create_list(new_list_name, user)

        article_buffer = list()
        for a in articles:
            article_buffer.append(Article.objects.get(id=ObjectId(a)))

        # Add selected article into new list and remove from old list
        List.objects(id=new_list.id).update_one(add_to_set__articles=article_buffer)
        List.objects(id=old_list.id).update_one(pull_all__articles=article_buffer)
    except Exception as e:
        print(type(e).__name__)
        return type(e).__name__

    old_list.reload()
    new_list.reload()
    return old_list, new_list


def copy_article_to_user_list(user, base_list_id, article_id, target_list_id):
    try:
        # Get article and lists
        article = Article.objects.get(id=ObjectId(article_id))
        list1 = List.objects.get(Q(id=ObjectId(base_list_id)) & Q(articles=article))
        list2 = List.objects.get(id=ObjectId(target_list_id))
        Vote(article=article, list=list2).save()
        # Update articles list
        List.objects(id=list2.id).update_one(push__articles=article)
    except Exception as e:
        return type(e).__name__


def merge_user_ist(user, base_list_id, target_list_id):
    try:
        base_list = List.objects.get(id=ObjectId(base_list_id))
        target_list = List.objects.get(id=ObjectId(target_list_id))

        List.objects(id=target_list.id).update_one(add_to_set__articles=base_list.articles)
        List.objects(id=base_list.id).delete()
    except Exception as e:
        return type(e).__name__


def invite_user(inviter, invitees_email, group_id):
    try:
        # Create new invitation object
        group = Group.objects.get(id=ObjectId(group_id))
        for invitee_email in invitees_email:
            if invitee_email != inviter.email:
                invitee = User.objects.get(email=invitee_email)
                Invitation(invitee=invitee, inviter=inviter, group=group).save()

    except Exception as e:
        return type(e).__name__


def get_user_pending_invitation(user):
    try:
        # Retrive all user pending invitaiton
        pending_invitations = Invitation.objects(invitee=user)
    except Exception as e:
        return type(e).__name__

    return pending_invitations


def accept_invitation(user, invitation_id):
    try:
        # Accept invitation
        invitation = Invitation.objects.get(id=ObjectId(invitation_id))
        if user != invitation.invitee:
            raise ValueError
        Group.objects(id=invitation.group.id).update_one(push__members=user)
        Invitation.objects(id=invitation.id).delete()
    except Exception as e:
        return type(e).__name__

    return invitation


def deny_invitation(user, invitation_id):
    try:
        # Accept invitation
        invitation = Invitation.objects.get(id=ObjectId(invitation_id))
        if user != invitation.invitee:
            raise ValueError
        Invitation.objects(id=invitation.id).delete()
    except Exception as e:
        return type(e).__name__

    return invitation
