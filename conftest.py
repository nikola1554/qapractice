from selenium import webdriver
import pytest
# from selenium.webdriver.chrome.options import Options  # with this import chrom doesn't work in headless mode
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    browser.maximize_window()
    return browser