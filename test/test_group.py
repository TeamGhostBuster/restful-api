import pytest
from test.conftest import *


@pytest.mark.run(after='test_delete_article_from_list')
@post('/group', {"name":"Awesome Group"})
def test_create_group(result=None):
    assert result.status_code == 200
    assert result.json()['name'] == 'Awesome Group'
    global_id['group_id'] = result.json()['id']

