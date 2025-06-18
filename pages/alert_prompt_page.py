from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

click_button_selector = (By.CLASS_NAME,'a-button')
result_input_selector = (By.ID, 'result-text')

class AlertPromptPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def press_click_button(self):
        self.find(click_button_selector).click()

    def check_result_text(self):
        return self.find(result_input_selector).text

    def send_some_text_in_prompt(self, text=''):
        wait = WebDriverWait(self.browser, timeout=2)
        alert = wait.until(lambda d: d.switch_to.alert)
        alert.send_keys(text)
        alert.accept()

    def decline_prompt(self):
        wait = WebDriverWait(self.browser, timeout=2)
        alert = wait.until(lambda d: d.switch_to.alert)
        alert.dismiss()