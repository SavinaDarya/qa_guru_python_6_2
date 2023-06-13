import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def window_size():
    browser.config.window_width = 1400
    browser.config.window_height = 600

@pytest.fixture
def browser_open():
    browser.open('https://google.com')


def test_yasha1urok(window_size,browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_mytest_wrong(window_size,browser_open):
    browser.element('[name="q"]').should(be.blank).type('4374377543954745656905768568569-53635-96ssdsdsd').press_enter()
    assert browser.element('.s6JM6d [data-ved]').should(have.text('2ahUKEwj1jpelzr__AhXbDhAIHQOdAmsQL3oECAcQAg'))
