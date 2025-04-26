from pages.base_page import BasePage
from selenium.webdriver.common.by import By

click_button_selector = (By.ID, 'submit-id-submit')
simple_button_link_selector = (By.LINK_TEXT, 'Simple button')
looks_like_a_button_link_selector = (By.XPATH, '//*[@href="/elements/button/like_a_button"]')
disabled_link_selector = (By.XPATH, '//*[@href="/elements/button/disabled"]')
result_text_selector = (By.ID,'result-text')

class ButtonsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_button(self):
        return self.find(click_button_selector)

    def press_click_button(self):
        self.click_button().click()

    def click_button_is_displayed(self):
        return self.click_button().is_displayed()

    def check_label_click_button(self):
        return self.click_button().get_attribute('value')

    def check_result_text(self):
        return self.find(result_text_selector).text

    def press_looks_like_a_button_tab(self):
        self.find(looks_like_a_button_link_selector).click()

    def press_disabled_tab(self):
        self.find(disabled_link_selector).click()