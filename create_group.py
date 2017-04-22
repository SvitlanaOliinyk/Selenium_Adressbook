import pytest
from model.group import Group
from web_api.adressbook_api import AdressbookAPI

@pytest.fixture()
def app():
    app = AdressbookAPI()
    yield app
    app.destroy()

def test_group(app):
    test_data_group = Group(name='Client', header='SuperHead', footer='Супер')
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(test_data_group)
    # TODO: Verify message for group creation
    app.return_to_group_page()
    app.logout()
    # TODO: Verify group in groplist


