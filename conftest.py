import pytest
from web_api.adressbook_api import AdressbookAPI
from model.group import Group

@pytest.fixture(scope='session')
def app():
    app = AdressbookAPI()
    yield app
    app.destroy()


@pytest.fixture(scope='session')
def init_login(app):
    app.session.login(username="admin", password="secret")
    yield
    app.session.logout()


@pytest.fixture()
def init_group(app, init_login):
    if not app.group.is_present():
        test_group = Group(name='Delete')
        app.group.create(test_group)