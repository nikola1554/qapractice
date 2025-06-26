import time

from pages.iframe_popup_page import IframePopUpPage
from pages.main_page import MainPage
from pages.popup_modal_page import PopUpModalPage

popup_title = 'I am a Pop-Up'
result_text_without_checkbox = 'None'
result_text_with_checkbox = 'select me or not'
result_incorrect_text = 'Nope. Better luck next time!'
result_correct_text = 'Correct!'
correct_background_color = '#d1e7dd'
incorrect_background_color = '#fff3cd'

def test_popup_modal_title_and_closing_by_x(browser):
    main_page = MainPage(browser)
    main_page.open_popup_modal_page()
    popup_modal_page = PopUpModalPage(browser)
    popup_modal_page.press_launch_popup_button()
    time.sleep(1)
    assert popup_title == popup_modal_page.check_popup_name()
    popup_modal_page.press_x_button_in_popup()
    time.sleep(1)
    assert not popup_modal_page.popup_is_displayed()

def test_popup_modal_send_with_checkbox(browser):
    main_page = MainPage(browser)
    main_page.open_popup_modal_page()
    popup_modal_page = PopUpModalPage(browser)
    popup_modal_page.press_launch_popup_button()
    time.sleep(1)
    popup_modal_page.mark_checkbox_in_popup()
    popup_modal_page.press_send_button_in_popup()
    time.sleep(1)
    assert result_text_with_checkbox == popup_modal_page.check_result_text()

def test_popup_modal_send_without_checkbox(browser):
    main_page = MainPage(browser)
    main_page.open_popup_modal_page()
    popup_modal_page = PopUpModalPage(browser)
    popup_modal_page.press_launch_popup_button()
    time.sleep(1)
    popup_modal_page.press_send_button_in_popup()
    time.sleep(1)
    assert result_text_without_checkbox == popup_modal_page.check_result_text()

def test_popup_modal_closing_by_close_button(browser):
    main_page = MainPage(browser)
    main_page.open_popup_modal_page()
    popup_modal_page = PopUpModalPage(browser)
    popup_modal_page.press_launch_popup_button()
    time.sleep(1)
    popup_modal_page.press_close_button_in_popup()
    time.sleep(1)
    assert not popup_modal_page.check_result_text_is_displayed()

def test_iframe_popup_correct_text(browser):
    main_page = MainPage(browser)
    main_page.open_popup_modal_page()
    popup_modal_page = PopUpModalPage(browser)
    popup_modal_page.open_iframe_popup_page()
    iframe_popup_page = IframePopUpPage(browser)
    iframe_popup_page.press_launch_popup_button()
    time.sleep(1)
    iframe_popup_page.switch_to_iframe()
    iframe_popup_page.copy_required_text_in_iframe()
    iframe_popup_page.press_check_button_in_iframe()
    iframe_popup_page.send_copied_text_to_input_field()
    iframe_popup_page.press_submit_button()
    assert result_correct_text == iframe_popup_page.check_result_text()
    assert correct_background_color == iframe_popup_page.check_background_color_of_result_text()

def test_iframe_popup_incorrect_text(browser):
    main_page = MainPage(browser)
    main_page.open_popup_modal_page()
    popup_modal_page = PopUpModalPage(browser)
    popup_modal_page.open_iframe_popup_page()
    iframe_popup_page = IframePopUpPage(browser)
    iframe_popup_page.press_launch_popup_button()
    time.sleep(1)
    iframe_popup_page.press_check_button_in_iframe()
    iframe_popup_page.send_copied_text_to_input_field()
    iframe_popup_page.press_submit_button()
    assert result_incorrect_text == iframe_popup_page.check_result_text()
    assert incorrect_background_color == iframe_popup_page.check_background_color_of_result_text()