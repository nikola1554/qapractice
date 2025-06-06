from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


input_field_selector = (By.ID, 'id_text_string')
result_input_selector = (By.ID, 'result-text')
error_message_selector = (By.ID, 'error_1_id_text_string')
email_field_tab_selector = (By.XPATH, '//*[@href="/elements/input/email"]')
password_field_tab_selector = (By.XPATH, '//*[@href="/elements/input/passwd"]')

class InputSimplePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.switch_to = None

    def input_field(self):
        return self.find(input_field_selector)

    def enter_value(self, text):
        self.input_field().send_keys(text)
        self.input_field().send_keys(Keys.ENTER)

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
        return self.input_field().get_attribute("validationMessage")

    def press_email_field_tab(self):
        self.find(email_field_tab_selector).click()

    def press_password_field_tab(self):
        self.find(password_field_tab_selector).click()