import pytest
import json
from web_api.adressbook_api import AdressbookAPI
from model.group import Group
from data.test_groups import test_groups
import os
from db_api.adressbook_orm import AdressbookORM

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")


@pytest.fixture(params=test_groups, ids=[repr(el) for el in test_groups])
def test_groups(request):
    return request.param

@pytest.fixture(scope="session")
def config(request):
    file_name = request.config.getoption("--config")
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_name) as f:
        return json.load(f)

@pytest.fixture(scope='session')
def app(request, config):
    browser = request.config.getoption("--browser")
    app = AdressbookAPI(browser=browser, base_url=config['web']["base_url"])
    yield app
    app.destroy()

@pytest.fixture(scope='session')
def db(config):
    dbfixture = AdressbookORM(**config['db'])
    yield dbfixture
    # dbfixture.destroy()
    pass

@pytest.fixture(scope='session')
def init_login(app, config):
    app.session.login(username=config['web']["username"], password=config['web']["password"])
    yield
    app.session.logout()


@pytest.fixture()
def init_group(app, init_login):
    if not app.group.is_present():
        test_group = Group(name='Delete')
        app.group.create(test_group)