from pages.base_page import BasePage
from selenium.webdriver.common.by import By

iframe_selector = (By.TAG_NAME,'iframe')
title_main_page_selector = (By.TAG_NAME,'h1')
title_iframe_page_selector = (By.TAG_NAME,'h1')

class IframePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.select = None

    def find_iframe(self):
        return self.find(iframe_selector)

    def switch_to_iframe_page(self):
        self.browser.switch_to.frame(self.find_iframe())

    def switch_to_main_page(self):
        self.browser.switch_to.default_content()

    def check_title_iframe_page(self):
        return self.find(title_iframe_page_selector).text

    def check_title_main_page(self):
        return self.find(title_main_page_selector).text