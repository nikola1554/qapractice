from pages.main_page import MainPage
from pages.single_checkbox_page import SingleCheckboxPage
from pages.mult_checkbox_page import MultCheckboxPage
import time

def test_single_checkbox(browser):
    main_page = MainPage(browser)
    main_page.open_single_checkbox_page()
    time.sleep(1)
    single_checkbox_page = SingleCheckboxPage(browser)
    assert len(single_checkbox_page.check_amount_of_checkboxes()) == 1, 'There are more than 1 checkboxes'
    assert 'Select me or not' == single_checkbox_page.check_checkbox_label(), 'checkbox has wrong label'
    assert single_checkbox_page.check_state_submit_button()
    single_checkbox_page.press_submit_button()
    assert not single_checkbox_page.result_text_is_displayed()
    single_checkbox_page.mark_single_checkbox()
    single_checkbox_page.press_submit_button()
    assert single_checkbox_page.result_text_is_displayed()
    assert single_checkbox_page.check_checkbox_label().lower() == single_checkbox_page.check_result_text()

def test_mult_checkbox(browser):
    main_page = MainPage(browser)
    main_page.open_single_checkbox_page()
    single_checkbox_page = SingleCheckboxPage(browser)
    single_checkbox_page.open_mult_checkbox_page()
    time.sleep(1)
    mult_checkbox_page = MultCheckboxPage(browser)
    assert len(mult_checkbox_page.check_amount_of_checkboxes()) == 3, 'Amount of checkboxes is not equal 3'
    assert 'one' == mult_checkbox_page.check_first_checkbox_label().lower(), 'first checkbox has wrong label'
    assert 'two' == mult_checkbox_page.check_second_checkbox_label().lower(), 'second checkbox has wrong label'
    assert 'three' == mult_checkbox_page.check_third_checkbox_label().lower(), 'third checkbox has wrong label'
    assert mult_checkbox_page.check_state_submit_button(), 'Button is not enabled or missing'
    mult_checkbox_page.press_submit_button()
    assert not mult_checkbox_page.result_text_is_displayed(), 'Result text is displayed'
    mult_checkbox_page.mark_first_checkbox()
    mult_checkbox_page.press_submit_button()
    assert mult_checkbox_page.result_text_is_displayed(), 'Result text is NOT displayed'
    assert mult_checkbox_page.check_first_checkbox_label().lower() == mult_checkbox_page.check_result_text()
    mult_checkbox_page.mark_second_checkbox()
    mult_checkbox_page.press_submit_button()
    assert mult_checkbox_page.check_second_checkbox_label().lower() == mult_checkbox_page.check_result_text()
    mult_checkbox_page.mark_third_checkbox()
    mult_checkbox_page.press_submit_button()
    assert mult_checkbox_page.check_third_checkbox_label().lower() == mult_checkbox_page.check_result_text()
    mult_checkbox_page.mark_first_checkbox()
    mult_checkbox_page.mark_third_checkbox()
    mult_checkbox_page.press_submit_button()
    assert mult_checkbox_page.check_first_checkbox_label().lower() + ', ' + mult_checkbox_page.check_third_checkbox_label().lower() == mult_checkbox_page.check_result_text()