from pages.base_page import BasePage
from selenium.webdriver.common.by import By

click_button_selector = (By.CLASS_NAME, 'a-button')
result_text_selector = (By.ID,'result-text')

class LikeAButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_button(self):
        return self.find(click_button_selector)

    def press_click_button(self):
        self.click_button().click()

    def click_button_is_displayed(self):
        return self.click_button().is_displayed()

    def check_text_click_button(self):
        return self.click_button().text

    def check_result_text(self):
        return self.find(result_text_selector).text