import json
import os.path
import pytest
from fixture.application import Application

fixture = None
target = None
target_path = None

@pytest.fixture
def app(request):
    global fixture
    global target
    global target_path

    browser = request.config.getoption("--browser")
    target_path = request.config.getoption("--targetpath")
    if target_path:
        path = target_path
    else:
        path = os.path.dirname(os.path.abspath(__file__))
    if target is None:
        config_file = os.path.join(path, request.config.getoption('--target'))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])

    fixture.session.ensure_login(name=target['username'], password=target["password"])
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--targetpath", action="store", default='C:\python_traning2020')