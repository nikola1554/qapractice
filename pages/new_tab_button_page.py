from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

click_button_selector = (By.ID, 'new-page-button')
result_input_selector = (By.ID, 'result-text')

class NewTabButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_button_new_tab_new_page(self):
        self.find(click_button_selector).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def check_url(self):
        return self.browser.current_url

    def check_result_text_is_displayed(self):
        try:
            return self.find(result_input_selector).text
        except NoSuchElementException:
            return False