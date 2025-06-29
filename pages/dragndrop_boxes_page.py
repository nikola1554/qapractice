from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

draggable_square_selector = (By.ID,"rect-draggable")
droppable_square_selector = (By.ID,"rect-droppable")
result_text_selector = (By.ID,"text-droppable")

class DragNDropBoxesPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def find_draggable_square(self):
        return self.find(draggable_square_selector)

    def find_droppable_square(self):
        return self.find(droppable_square_selector)

    def move_draggable_square_to_droppable_square(self):
        ActionChains(self.browser).drag_and_drop(self.find_draggable_square(), self.find_droppable_square()).perform()

    def find_result_text(self):
        return self.find(result_text_selector).text