from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


email_field_selector = (By.ID, 'id_email')
result_input_selector = (By.ID, 'result-text')
error_message_selector = (By.ID, 'error_1_id_email')

class InputEmailPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def email_field(self):
        return self.find(email_field_selector)

    def enter_email(self, email):
        self.email_field().send_keys(email)
        self.email_field().send_keys(Keys.ENTER)

    def find_result_text(self):
        return self.find(result_input_selector)

    def check_result_text(self):
        return self.find_result_text().text

    def check_result_text_is_displayed(self):
        try:
            return self.find_result_text().is_displayed()
        except NoSuchElementException:
            return False

    def error_message(self):
        return self.find(error_message_selector)

    def check_error_message_text(self):
        try:
            return self.error_message().text
        except NoSuchElementException:
            return 'error message is not present on the page'

    def check_tooltip_message(self):
        return self.email_field().get_attribute("validationMessage")