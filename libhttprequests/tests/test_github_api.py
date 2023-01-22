from libhttprequests.github_api import get_github_avatar


def test_github_avatar():
    result = get_github_avatar('mauriciodoerr')
    assert '28199933' in result
