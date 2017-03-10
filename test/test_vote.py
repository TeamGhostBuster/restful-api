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
