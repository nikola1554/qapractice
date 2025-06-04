from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

first_checkbox_selector = (By.ID, 'id_checkboxes_0')
second_checkbox_selector = (By.ID, 'id_checkboxes_1')
third_checkbox_selector = (By.ID, 'id_checkboxes_2')
text_first_checkbox_selector = (By.XPATH,'//*[@for="id_checkboxes_0"]')
text_second_checkbox_selector = (By.XPATH,'//*[@for="id_checkboxes_1"]')
text_third_checkbox_selector = (By.XPATH,'//*[@for="id_checkboxes_2"]')
submit_button_selector = (By.ID, 'submit-id-submit')
result_text_selector = (By.ID, 'result-text')

class MultCheckboxPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def first_checkbox(self):
        return self.find(first_checkbox_selector)

    def mark_first_checkbox(self):
        self.first_checkbox().click()

    def second_checkbox(self):
        return self.find(second_checkbox_selector)

    def mark_second_checkbox(self):
        self.second_checkbox().click()

    def third_checkbox(self):
        return self.find(third_checkbox_selector)

    def mark_third_checkbox(self):
        self.third_checkbox().click()

    def check_amount_of_checkboxes(self):
        return self.browser.find_elements(By.CSS_SELECTOR,'.form-check-input')

    def check_first_checkbox_label(self):
        return self.find(text_first_checkbox_selector).text

    def check_second_checkbox_label(self):
        return self.find(text_second_checkbox_selector).text

    def check_third_checkbox_label(self):
        return self.find(text_third_checkbox_selector).text

    def submit_button(self):
        return self.find(submit_button_selector)

    def press_submit_button(self):
        self.submit_button().click()

    def check_state_submit_button(self):
        return self.submit_button().is_enabled()

    def result_text_is_displayed(self):
        try:
            return self.find(result_text_selector).is_displayed()
        except NoSuchElementException:
            return False

    def check_result_text(self):
        return self.find(result_text_selector).text