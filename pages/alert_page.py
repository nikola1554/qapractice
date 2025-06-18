from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

click_button_selector = (By.CLASS_NAME,'a-button')
confirm_page_link_selector = (By.XPATH,'//*[@href="/elements/alert/confirm"]')
prompt_page_link_selector = (By.XPATH,'//*[@href="/elements/alert/prompt"]')

class AlertPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def press_click_button(self):
        self.find(click_button_selector).click()

    def get_alert_text(self):
        wait = WebDriverWait(self.browser, timeout=2)
        alert = wait.until(lambda d: d.switch_to.alert)
        text = alert.text
        alert.accept()
        return text

    def open_confirm_page(self):
        self.find(confirm_page_link_selector).click()

    def open_prompt_page(self):
        self.find(prompt_page_link_selector).click()