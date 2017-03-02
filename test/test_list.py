from test.conftest import *
import pytest


@pytest.mark.run(order=1)
@post('/user/list', {'name': 'Test List'})
def test_create_user_list(result=None):
    assert result.status_code == 200
    assert result.json()['name'] == 'Test List'
    global list_id
    list_id = result.json()['id']
    global_id['list_id'] = result.json()['id']


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


@pytest.mark.run(after='test_create_article_for_user')
@delete('/user/list/{}/article/{}')
def test_delete_article_from_list(result=None, url_id=['list_id', 'article_id']):
    assert result.status_code == 200
    assert not any(a == global_id['article_id'] for a in result.json()['articles']) is True
