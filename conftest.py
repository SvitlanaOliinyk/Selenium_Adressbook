import pytest
from web_api.adressbook_api import AdressbookAPI

@pytest.fixture(scope='session')
def app():
    app = AdressbookAPI()
    app.login(username="admin", password="secret")
    yield app
    app.logout()
    app.destroy()