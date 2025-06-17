from pages.base_page import BasePage
from selenium.webdriver.common.by import By

result_input_selector = (By.ID, 'result-text')

class NewTabNewPagePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def check_url(self):
        return self.browser.current_url

    def check_result_text(self):
        return self.find(result_input_selector).text

    def switch_to_previous_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[0])