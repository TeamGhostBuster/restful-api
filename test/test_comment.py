import pytest
from test.conftest import *


@pytest.mark.run(after='test_create_article_for_user')
@post('/article/{}/comment', {"comment": "shit posting #1"})
def test_post_comment_to_article(result=None, url_id=['article_id']):
    assert result.status_code == 200
    assert result.json()['content'] == 'shit posting #1'
