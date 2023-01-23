import pytest

from libhttprequests.spam.db import DBConnection
from libhttprequests.spam.models import User


@pytest.fixture(scope='module')
def connection():
    # Setup
    db_connection = DBConnection()
    # Tear Down
    yield db_connection
    db_connection.close()


@pytest.fixture
def session(connection):
    # Setup
    db_session = connection.generate_session()
    yield db_session
    # Tear Down
    db_session.roll_back()
    db_session.close()


def test_save_user(session):
    user = User(name='User One')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='User One'), User(name='User Two')]
    for user in users:
        session.save(user)
    assert users == session.list()
