from test.conftest import *
import pytest


@pytest.mark.run(order=1)
@post('/user/list', {"name": "Test List"})
def test_create_user_list(result=None):
    assert result.status_code == 200
    assert result.json()['name'] == 'Test List'
    global list_id
    list_id = result.json()['id']
    global_id['list_id'] = result.json()['id']


@pytest.mark.run(after='test_create_user_list')
@put('/user/list/{}/rename', {"name": "Rename Test List"})
def test_rename_list(result=None, url_id=['list_id']):
    assert result.status_code == 200


@pytest.mark.run(after='test_create_user_list')
@delete('/user/list/{}/archive')
def test_archive_user_list(result=None, url_id=['list_id']):
    assert result.status_code == 200
    assert [l['archived'] for l in result.json()['lists'] if l['id'] == list_id][0] is True


@pytest.mark.run(after='test_archive_user_list')
@put('/user/list/{}/retrieve')
def test_retrieve_user_list(result=None, url_id=['list_id']):
    assert result.status_code == 200
    assert [l['archived'] for l in result.json()['lists'] if l['id'] == list_id][0] is False


@pytest.mark.run(after='test_create_user_list')
@get('/user/lists')
def test_get_user_all_lists(result=None):
    assert result.status_code == 200
    assert any(l['id'] == list_id for l in result.json()['lists']) is True


@pytest.mark.run(after='test_post_comment_to_article')
@delete('/user/list/{}/article/{}')
def test_delete_article_from_list(result=None, url_id=['list_id', 'article_id']):
    assert result.status_code == 200
    assert not any(a == global_id['article_id'] for a in result.json()['articles']) is True


@pytest.mark.run(after='test_create_group')
@post('/group/list', '{{"name": "Awesome Group List", "group_id":"{}"}}')
def test_create_group_list(result=None, ids=['group_id']):
    assert result.status_code == 200
    assert result.json()['name'] == 'Awesome Group List'
    global_id['group_list_id'] = result.json()['id']


@pytest.mark.run(after='test_create_group_list')
@post('/group/{}/list/{}/article', {"title":"awesome group article", "description":"whatever"})
def test_create_article_for_group(result=None, url_id=['group_id', 'group_list_id']):
    assert result.status_code == 200
    assert result.json()['title'] == 'awesome group article'
    assert result.json()['description'] == 'whatever'
    global_id['group_article_id'] = result.json()['id']
