from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

new_page_link_selector = (By.XPATH, '//*[@href="/elements/new_tab/new_page"]')
open_new_tab_button_page_selector = (By.XPATH, '//*[@href="/elements/new_tab/button"]')
result_input_selector = (By.ID, 'result-text')

class NewTabLinkPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_link_new_tab_new_page(self):
        self.find(new_page_link_selector).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def open_new_tab_button_page(self):
        self.find(open_new_tab_button_page_selector).click()

    def check_url(self):
        return self.browser.current_url

    def check_result_text_is_displayed(self):
        try:
            return self.find(result_input_selector).text
        except NoSuchElementException:
            return False

