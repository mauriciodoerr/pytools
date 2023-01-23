from libhttprequests.spam.db import DBConnection
from libhttprequests.spam.models import User


def test_save_user():
    connection = DBConnection()
    session = connection.generate_session()
    user = User(name='User One')
    session.save(user)
    assert isinstance(user.id, int)
    session.roll_back()
    session.close()
    connection.close()


def test_list_users():
    connection = DBConnection()
    session = connection.generate_session()
    users = [User(name='User One'), User(name='User Two')]
    for user in users:
        session.save(user)
    assert users == session.list()
    session.roll_back()
    session.close()
    connection.close()
