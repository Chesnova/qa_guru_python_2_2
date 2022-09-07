import pytest
from selene import have, be
from selene.support import by
from selene.support.shared import browser

@pytest.fixture
def open_browser():
    browser.config.timeout = 3
    browser.config.base_url = ('https://demoqa.com')

def test_submit_user_details(open_browser):
    browser.open('/text-box')
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Text Box'))
    browser.element(by.text('Text Box')).should(be.visible)

    browser.all('#userForm input, #userForm textarea').should(have.size(4))
    browser.element('#userForm').all('input, textarea').should(have.size(4))

    browser.element('#userName').set_value('name')
    browser.element('#submit').click()
