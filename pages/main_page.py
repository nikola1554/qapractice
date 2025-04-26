from pages.base_page import BasePage
from selenium.webdriver.common.by import By

url = 'https://www.qa-practice.com/'
text_input_link_selector = (By.LINK_TEXT, 'Text input')
simple_button_link_selector = (By.LINK_TEXT, 'Simple button')


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_main_page(self):
        self.browser.get(url)

    def open_input_field_page_text_input_tab(self):
        self.browser.get(url)
        self.find(text_input_link_selector).click()

    def open_buttons_page(self):
        self.browser.get(url)
        self.find(simple_button_link_selector).click()

