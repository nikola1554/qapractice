import time

from pages.dragndrop_boxes_page import DragNDropBoxesPage
from pages.main_page import MainPage

result_text = 'Dropped!'

def test_drag_n_drop_squares(browser):
    main_page = MainPage(browser)
    main_page.open_dragndrop_boxes_page()
    dragndrop_boxes_page = DragNDropBoxesPage(browser)
    dragndrop_boxes_page.move_draggable_square_to_droppable_square()
    assert result_text == dragndrop_boxes_page.find_result_text()
