import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 2220
    browser.config.window_height = 1080
    browser.config.base_url = 'http://demoqa.com'

    yield
    browser.quit()
