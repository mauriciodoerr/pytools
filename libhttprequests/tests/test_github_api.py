from unittest.mock import Mock

from libhttprequests import github_api
from libhttprequests.github_api import get_github_avatar


def test_github_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login": "mauriciodoerr",
        "id": 28199933,
        "avatar_url": "https://avatars.githubusercontent.com/u/28199933?v=4"
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    result = get_github_avatar('mauriciodoerr')
    assert '28199933' in result
