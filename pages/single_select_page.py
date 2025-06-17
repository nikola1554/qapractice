from selenium.common import NoSuchElementException
import random
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

select_field_selector = (By.ID, 'id_choose_language')
submit_button_selector = (By.ID, 'submit-id-submit')
result_text_selector = (By.ID,'result-text')
multiple_select_tab_selector = (By.XPATH, '//*[@href="/elements/select/mult_select"]')

class SingleSelectPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.select = None

    def find_select_field(self):
        select_element = self.find(select_field_selector)
        select = Select(select_element)
        return select

    def find_submit_button(self):
        return self.find(submit_button_selector)

    def choose_random_option(self):
        amount_selects = self.browser.find_elements(By.TAG_NAME, 'option')
        random_index = random.randint(1,len(amount_selects)-1)
        self.find_select_field().select_by_index(random_index)
        random_option_text = self.browser.find_element(By.XPATH,f'//option[contains(@value,{random_index})]').text
        self.find_submit_button().click()
        return random_option_text

    def check_result_text(self):
        return self.find(result_text_selector).text

    def choose_empty_option(self):
        self.find_select_field().select_by_value('2')
        self.find_select_field().select_by_index(0)
        self.find_submit_button().click()

    def check_result_text_is_displayed(self):
        try:
            return self.check_result_text().is_displayed()
        except NoSuchElementException:
            return False

    def press_multiple_select_tab(self):
        self.find(multiple_select_tab_selector).click()

    def check_tooltip_message(self):
        return self.find(select_field_selector).get_attribute("validationMessage")
