from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(2)
    browser.maximize_window()
    yield browser
    browser.quit()
