from selenium.webdriver.support.color import Color

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

launch_popup_button_selector = (By.CLASS_NAME, 'btn')
iframe_selector = (By.TAG_NAME,'iframe')
text_to_copy_selector = (By.ID,'text-to-copy')
check_button_selector = (By.XPATH, '//button[@form="empty-form"]')
input_field_selector = (By.ID,'id_text_from_iframe')
submit_button_selector = (By.ID,'submit-id-submit')
result_text_selector = (By.ID,'check-result')
copied_text_from_iframe = 'Some text'


class IframePopUpPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def press_launch_popup_button(self):
        self.find(launch_popup_button_selector).click()

    def switch_to_iframe(self):
        iframe = self.find(iframe_selector)
        self.browser.switch_to.frame(iframe)

    def copy_required_text_in_iframe(self):
        global copied_text_from_iframe
        copied_text_from_iframe = self.find(text_to_copy_selector).text

    def press_check_button_in_iframe(self):
        self.browser.switch_to.default_content()
        self.find(check_button_selector).click()

    def send_copied_text_to_input_field(self):
        self.find(input_field_selector).send_keys(copied_text_from_iframe)

    def press_submit_button(self):
        self.find(submit_button_selector).click()

    def check_result_text(self):
        return self.find(result_text_selector).text

    def check_background_color_of_result_text(self):
        return Color.from_string(self.find(result_text_selector).value_of_css_property('background-color')).hex