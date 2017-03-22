import pytest
from test.conftest import *


@pytest.mark.run(after='test_create_article_for_group')
@post('/group/{}/list/{}/article/{}/upvote')
def test_upvote_article(result=None, url_id=['group_id', 'group_list_id', 'group_article_id']):
    assert result.status_code == 200
    assert result.json()['vote_count'] == 1


@pytest.mark.run(after='test_upvote_article')
@post('/group/{}/list/{}/article/{}/upvote')
def test_user_cannot_vote_twice(result=None, url_id=['group_id', 'group_list_id', 'group_article_id']):
    assert result.status_code == 403


@pytest.mark.run(after='test_user_cannot_vote_twice')
@post('/group/{}/list/{}/article/{}/downvote')
def test_downvote_article(result=None, url_id=['group_id', 'group_list_id', 'group_article_id']):
    assert result.status_code == 200
    assert result.json()['vote_count'] == 0


@pytest.mark.run(after='test_downvote_article')
@put('/user/list/{}/partition', '{{"name": "New Group List", "articles":["{}"]}}')
def test_partition_list(result=None, url_id=['group_list_id'], ids=['group_article_id']):
    assert result.status_code == 200
    global_id['new_list_id'] = result.json()['new_list']['id']
    global_id['old_list_id'] = result.json()['old_list']['id']


@pytest.mark.run(after='test_partition_list')
@put('/user/list/{}/article/{}/copy/list/{}')
def test_copy_article(result=None, url_id=['new_list_id', 'group_article_id', 'old_list_id']):
    assert result.status_code == 200


@pytest.mark.run(after='test_copy_article')
@put('/user/list/{}/merge/list/{}')
def test_merge_list(result=None, url_id=['new_list_id', 'old_list_id']):
    assert result.status_code == 200


@pytest.mark.run(after='test_create_group')
@post('/share/list', '{{"list_id":"{}", "group_id":["{}"]}}')
def test_share_list_to_group(result=None, json_id=['list_id', 'group_id']):
    assert result.status_code == 200
