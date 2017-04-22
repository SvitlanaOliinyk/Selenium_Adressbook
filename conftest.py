import pytest
from web_api.adressbook_api import AdressbookAPI

@pytest.fixture()
def app():
    app = AdressbookAPI()
    app.login(username="admin", password="secret")
    yield app
    app.logout()
    app.destroy()