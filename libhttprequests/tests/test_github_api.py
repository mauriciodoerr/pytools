from unittest.mock import Mock

import pytest

from libhttprequests import github_api
from libhttprequests.github_api import get_github_avatar


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/28199933?v=4'
    resp_mock.json.return_value = {
        'login': 'mauricio',
        'id': 28199933,
        'avatar_url': url
    }
    github_original_api = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = github_original_api


def test_github_avatar(avatar_url):
    result = get_github_avatar('mauriciodoerr')
    assert '28199933' in result


def test_github_avatar_integrated():
    result = get_github_avatar('mauriciodoerr')
    assert '28199933' in result
