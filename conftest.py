import pytest
import json
import os.path
from fixtures.application import Application
from fixtures.db import DbFixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))

@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    web = config['web']
    web_admin = config['webadmin']
    print(web)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web['baseUrl'])
    fixture.session.ensure_login(username=web_admin['username'], password=web_admin['password'])
    return fixture

@pytest.fixture(scope="session")
def db(request, config):
    db_config = config['db']
    dbfixture = DbFixture(host=db_config['host'], port=db_config['port'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope="session", autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")