from selenium.common import NoSuchElementException
import random
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

place_field_selector = (By.ID, 'id_choose_the_place_you_want_to_go')
vehicles_field_selector = (By.ID, 'id_choose_how_you_want_to_get_there')
times_field_selector = (By.ID, 'id_choose_when_you_want_to_go')
submit_button_selector = (By.ID, 'submit-id-submit')
result_text_selector = (By.ID,'result-text')
places_list_selector = '//*[@id="id_choose_the_place_you_want_to_go"]/child::option'
vehicles_list_selector = '//*[@id="id_choose_how_you_want_to_get_there"]/child::option'
times_list_selector = '//*[@id="id_choose_when_you_want_to_go"]/child::option'

class MultipleSelectPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.select = None

    def find_select_field(self,select_field_selector):
        select_element = self.find(select_field_selector)
        select = Select(select_element)
        return select

    def find_submit_button(self):
        return self.find(submit_button_selector)

    def press_submit_button(self):
        self.find_submit_button().click()

    def choose_random_option(self,objects_list,select_field_selector):
        amount_objects = self.browser.find_elements(By.XPATH, objects_list)
        random_object_index = random.randint(1, len(amount_objects) - 1)
        self.find_select_field(select_field_selector).select_by_index(random_object_index)
        return self.browser.find_element(By.XPATH,f'{objects_list}[contains(@value,{random_object_index})]').text.lower()

    def fill_with_random_options(self):
        random_place = self.choose_random_option(places_list_selector,place_field_selector)
        random_vehicle = self.choose_random_option(vehicles_list_selector,vehicles_field_selector)
        random_time = self.choose_random_option(times_list_selector,times_field_selector)
        self.find_submit_button().click()
        return f'to go by {random_vehicle} to the {random_place} {random_time}'

    def check_result_text(self):
        return self.find(result_text_selector).text

    def check_tooltip_message(self,select_field):
        return self.find(select_field).get_attribute("validationMessage")

    def check_result_text_is_displayed(self):
        try:
            return self.check_result_text().is_displayed()
        except NoSuchElementException:
            return False