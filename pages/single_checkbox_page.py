from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

single_checkbox_selector = (By.ID, 'id_checkbox_0')
text_single_checkbox_selector = (By.CLASS_NAME,'form-check-label')
submit_button_selector = (By.ID, 'submit-id-submit')
result_text_selector = (By.ID, 'result-text')
mult_checkboxes_tub_selector = (By.XPATH, '//*[@class="tab"]')

class SingleCheckboxPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def single_checkbox(self):
        return self.find(single_checkbox_selector)

    def mark_single_checkbox(self):
        self.single_checkbox().click()

    def check_amount_of_checkboxes(self):
        return self.browser.find_elements(By.XPATH, '//input[@type="checkbox"]')

    def check_checkbox_label(self):
        return self.find(text_single_checkbox_selector).text

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

    def open_mult_checkbox_page(self):
        self.find(mult_checkboxes_tub_selector).click()
