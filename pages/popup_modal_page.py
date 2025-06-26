from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

launch_popup_button_selector = (By.CLASS_NAME, 'btn')
popup_name_selector = (By.ID, 'exampleModalLabel')
x_button_in_popup_selector = (By.CLASS_NAME, 'btn-close')
close_button_selector = (By.XPATH, "//button[@class='btn btn-secondary' and contains(text(), 'Close')]")
send_button_selector = (By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'Send')]")
checkbox_selector = (By.XPATH, "//input[@id='id_checkbox_0']")
result_text_selector = (By.ID,'result-text')
iframe_popup_link_selector = (By.XPATH,'//*[@href="/elements/popup/iframe_popup"]')

class PopUpModalPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def press_launch_popup_button(self):
        self.find(launch_popup_button_selector).click()

    def check_popup_name(self):
        return self.find(popup_name_selector).text

    def press_x_button_in_popup(self):
        self.find(x_button_in_popup_selector).click()

    def popup_is_displayed(self):
        return self.find(popup_name_selector).is_displayed()

    def press_close_button_in_popup(self):
        self.find(close_button_selector).click()

    def press_send_button_in_popup(self):
        self.find(send_button_selector).click()

    def mark_checkbox_in_popup(self):
        self.find(checkbox_selector).click()

    def check_result_text_is_displayed(self):
        try:
            return self.find(result_text_selector).is_displayed()
        except NoSuchElementException:
            return False

    def check_result_text(self):
        return self.find(result_text_selector).text

    def open_iframe_popup_page(self):
        self.find(iframe_popup_link_selector).click()