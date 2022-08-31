from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture()
def open_browser():
    browser.open('https://google.com/ncr')

def test_should_find_element(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_shouldnt_find_element(open_browser):
    browser.element('[name="q"]').should(be.blank).type('slkrtetw').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))
