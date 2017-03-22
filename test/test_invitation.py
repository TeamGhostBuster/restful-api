import pytest
from test.conftest import *


@pytest.mark.order(after='test_create_group')
@post('/group/{}/invite', {"email": ["zichun3@ualberta.ca"]})
def test_invite_member(result=None, url_id=['group_id']):
    assert result.status_code == 200
