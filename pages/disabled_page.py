from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

submit_button_selector = (By.ID, 'submit-id-submit')
drop_down_selector = (By.ID, 'id_select_state')
result_text_selector = (By.ID, 'result-text')


class DisabledPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def submit_button(self):
        return self.find(submit_button_selector)

    def check_state_submit_button(self):
        return self.submit_button().is_enabled()

    def drop_down(self):
        return self.find(drop_down_selector)

    def switch_to_enabled_state_drop_down(self):
        Select(self.drop_down()).select_by_value('enabled')

    def switch_to_disabled_state_drop_down(self):
        Select(self.drop_down()).select_by_value('disabled')

    def press_submit_button(self):
        self.submit_button().click()

    def check_result_text(self):
        return self.find(result_text_selector).text