"""Module contains browser fixture."""
from pytest import fixture
from lib.web.connection.browser import Browser

_command_executor: str = 'http://localhost:9515'


@fixture(scope='module')
def browser(request) -> Browser:
    browser = Browser(url=_command_executor)
    request.addfinalizer(browser.close)
    return browser
