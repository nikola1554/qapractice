from pages.main_page import MainPage
from pages.multiple_select_page import MultipleSelectPage, place_field_selector, vehicles_field_selector, times_field_selector, places_list_selector, vehicles_list_selector
from pages.single_select_page import SingleSelectPage

validation_error_text = 'Please select an item in the list.'

def test_random_single_select(browser):
    main_page = MainPage(browser)
    main_page.open_select_page()
    single_select_page = SingleSelectPage(browser)
    assert single_select_page.choose_random_option() == single_select_page.check_result_text()

def test_single_select_validation_error(browser):
    main_page = MainPage(browser)
    main_page.open_select_page()
    single_select_page = SingleSelectPage(browser)
    single_select_page.choose_empty_option()
    assert validation_error_text == single_select_page.check_tooltip_message()
    assert False == single_select_page.check_result_text_is_displayed()

def test_random_multiple_select(browser):
    main_page = MainPage(browser)
    main_page.open_select_page()
    single_select_page = SingleSelectPage(browser)
    single_select_page.press_multiple_select_tab()
    multiple_select_page = MultipleSelectPage(browser)
    assert multiple_select_page.fill_with_random_options() == multiple_select_page.check_result_text()

def test_multiple_select_validation_errors(browser):
    main_page = MainPage(browser)
    main_page.open_select_page()
    single_select_page = SingleSelectPage(browser)
    single_select_page.press_multiple_select_tab()
    multiple_select_page = MultipleSelectPage(browser)
    multiple_select_page.press_submit_button()
    assert validation_error_text == multiple_select_page.check_tooltip_message(place_field_selector)
    assert False == multiple_select_page.check_result_text_is_displayed()
    multiple_select_page.choose_random_option(places_list_selector,place_field_selector)
    multiple_select_page.press_submit_button()
    assert validation_error_text == multiple_select_page.check_tooltip_message(vehicles_field_selector)
    assert False == multiple_select_page.check_result_text_is_displayed()
    multiple_select_page.choose_random_option(vehicles_list_selector,vehicles_field_selector)
    multiple_select_page.press_submit_button()
    assert validation_error_text == multiple_select_page.check_tooltip_message(times_field_selector)
    assert False == multiple_select_page.check_result_text_is_displayed()