import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def size_window():
    browser.config.window_width = 1900
    browser.config.window_height = 1200
    yield
