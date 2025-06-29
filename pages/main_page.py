from pages.base_page import BasePage
from selenium.webdriver.common.by import By

url = 'https://www.qa-practice.com/'
text_input_link_selector = (By.LINK_TEXT, 'Text input')
simple_button_link_selector = (By.LINK_TEXT, 'Simple button')
single_ui_elements_list_selector = (By.CLASS_NAME, 'has-sub')
single_checkbox_page_selector = (By.XPATH, '//*[@href="/elements/checkbox"]')
new_tab_link_page_selector = (By.XPATH, '//*[@href="/elements/new_tab"]')
alert_page_selector = (By.XPATH, '//*[@href="/elements/alert"]')
single_select_page_selector = (By.XPATH, '//*[@href="/elements/select/single_select"]')
iframe_page_selector = (By.XPATH, '//*[@href="/elements/iframe/iframe_page"]')
popup_modal_page_selector = (By.XPATH, '//*[@href="/elements/popup"]')
dragndrop_page_selector = (By.XPATH, '//*[@href="/elements/dragndrop"]')

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_main_page(self):
        self.browser.get(url)

    def open_input_field_page_text_input_tab(self):
        self.browser.get(url)
        self.find(text_input_link_selector).click()

    def open_buttons_page(self):
        self.browser.get(url)
        self.find(simple_button_link_selector).click()

    def single_ui_elements_list(self):
        return self.find(single_ui_elements_list_selector)

    def single_checkbox_page(self):
        return self.find(single_checkbox_page_selector)

    def open_single_checkbox_page(self):
        self.browser.get(url)
        self.single_ui_elements_list().click()
        self.single_checkbox_page().click()

    def open_new_tab_link_page(self):
        self.browser.get(url)
        self.single_ui_elements_list().click()
        self.find(new_tab_link_page_selector).click()

    def open_alert_page(self):
        self.browser.get(url)
        self.single_ui_elements_list().click()
        self.find(alert_page_selector).click()

    def open_select_page(self):
        self.open_main_page()
        self.find(single_select_page_selector).click()
        
    def open_iframe_page(self):
        self.open_main_page()
        self.single_ui_elements_list().click()
        self.find(iframe_page_selector).click()

    def open_popup_modal_page(self):
        self.open_main_page()
        self.single_ui_elements_list().click()
        self.find(popup_modal_page_selector).click()

    def open_dragndrop_boxes_page(self):
        self.open_main_page()
        self.single_ui_elements_list().click()
        self.find(dragndrop_page_selector).click()
