from test.conftest import *
import pytest


@pytest.mark.run(after='test_create_user_list')
@post('/user/list/{}/article', '{{"title":"Test Article", "description": "asshole" }}')
def test_create_article_for_user(result=None, url_id=['list_id']):
    print(result.json())
    assert result.status_code == 200
    assert result.json()['title'] == 'Test Article'
    # save it for more further testing
    global article_id
    article_id = result.json()['id']
    global_id['article_id'] = article_id
