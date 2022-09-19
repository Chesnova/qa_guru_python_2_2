import pytest
from selene import have, be, command
from selene.support import by
from selene.support.shared import browser



@pytest.fixture
def open_browser():
    browser.config.timeout = 3
    browser.config.base_url = ('https://demoqa.com')

def given_app_opened():
    browser.open('/text-box')
    # отключение рекламы
    # ads = browser.all('[id^=google_ads_][id$=container__]')
    # ads.should(have.size_greater_than_or_equal(3))
    # ads[0]._execute_script('element.remove()')
    # ads[0].perform(command.js.remove) можно так написать

    # if ads.wait.until(have.size_greater_than_or_equal(3)): если дождется, то удалит, если нет, то не упадет
    #   ads[0]._execute_script('element.remove()')
    # wait.until можно заменить на matching

    # отключение рекламы
    browser.execute_script(
        'document.querySelectorAll("[id^=google_ads_][id$=container__]").forEach(element => element.remove())')


def test_submit_user_details(open_browser):
    given_app_opened()
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Text Box'))
    browser.element(by.text('Text Box')).should(be.visible)

    browser.all('#userForm input, #userForm textarea').should(have.size(4))
    browser.element('#userForm').all('input, textarea').should(have.size(4))

    browser.element('#userName').set_value('name')
    browser.element('#submit').click()
    # browser.element('#submit').perform(command.js.click) можно сделать с помощью джаваскрипта
    # submit = browser.element(('#submit')).with_(click_by_js=True) можно сделать с помощью джаваскрипта
    # submit.click()

    slow_browser = browser.with_(timeout=3)
    slow_browser.element('.main-header').should(have.text('Text Box'))
    browser.with_(timeout=2).all('#userForm input, #userForm textarea').should(have.size(4))

    browser.all('.form-label').filter_by(have.text('Address'))[1].should(have.text('Permanent Address'))
