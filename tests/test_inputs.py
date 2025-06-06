from pages.input_email_page import InputEmailPage
from pages.input_password_page import InputPasswordPage
from pages.input_simple_page import InputSimplePage
from pages.main_page import MainPage

empty_value = ''
invalid_value = 'Hello!'
error_message_invalid_value = 'Enter a valid string consisting of letters, numbers, underscores or hyphens.'
less_than_min_value = 1
error_message_less_than_min_value = 'Please enter 2 or more characters'
min_value = 'We'
max_value = 'eW_rLrt234y-Psgty765_gmrt'
more_than_max_value = 'weerLrt234yhPsgty765tgmrt2'
error_message_more_than_max_value = 'Please enter no more than 25 characters'
tooltip_message = 'Please fill out this field.'
valid_email = 'test@mail.com'
email_without_symbol_at = 'testmail.com'
email_without_symbol_dot = 'test@mailcom'
too_short_email = 'e@e.e'
error_message_invalid_email = 'Enter a valid email address.'
valid_password = 'sF#8leJ@'
password_without_digits = 'sF#qleJ@'
password_without_lowercase_English_letter = 'SF#8LEJ@'
error_message_invalid_password = 'Low password complexity'


def test_input_field_check_max_length_limit(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.enter_value(max_value)
    assert max_value == input_simple_page.check_result_text()

def test_input_field_check_min_length_limit(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.enter_value(min_value)
    assert min_value == input_simple_page.check_result_text()


def test_input_field_check_less_than_min_length_limit(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.enter_value(less_than_min_value)
    assert False == input_simple_page.check_result_text_is_displayed()
    assert error_message_less_than_min_value == input_simple_page.check_error_message_text()

def test_input_field_check_more_than_max_length_limit(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.enter_value(more_than_max_value)
    assert False == input_simple_page.check_result_text_is_displayed()
    assert error_message_more_than_max_value == input_simple_page.check_error_message_text()

def test_input_field_check_invalid_symbols(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.enter_value(invalid_value)
    assert False == input_simple_page.check_result_text_is_displayed()
    assert error_message_invalid_value == input_simple_page.check_error_message_text()

# to work with tooltips - need to find element and apply method get attribute with message "validationMessage"
def test_input_field_check_empty_value(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.enter_value(empty_value)  # it also works without this step
    assert tooltip_message == input_simple_page.check_tooltip_message()
    assert False == input_simple_page.check_result_text_is_displayed()

def test_email_field_enter_valid_email(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.press_email_field_tab()
    input_email_page = InputEmailPage(browser)
    input_email_page.enter_email(valid_email)
    assert valid_email == input_email_page.check_result_text()

def test_email_field_enter_email_without_at_symbol(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.press_email_field_tab()
    input_email_page = InputEmailPage(browser)
    input_email_page.enter_email(email_without_symbol_at)
    assert False == input_email_page.check_result_text_is_displayed()
    assert error_message_invalid_email == input_email_page.check_error_message_text()

def test_email_field_enter_email_without_dot_symbol(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.press_email_field_tab()
    input_email_page = InputEmailPage(browser)
    input_email_page.enter_email(email_without_symbol_dot)
    assert False == input_email_page.check_result_text_is_displayed()
    assert error_message_invalid_email == input_email_page.check_error_message_text()

def test_email_field_enter_too_short_email(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.press_email_field_tab()
    input_email_page = InputEmailPage(browser)
    input_email_page.enter_email(too_short_email)
    assert False == input_email_page.check_result_text_is_displayed()
    assert error_message_invalid_email == input_email_page.check_error_message_text()

def test_email_field_check_empty_value(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.press_email_field_tab()
    input_email_page = InputEmailPage(browser)
    input_email_page.enter_email(empty_value)
    assert tooltip_message == input_email_page.check_tooltip_message()
    assert False == input_email_page.check_result_text_is_displayed()

def test_password_field_enter_valid_email(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.press_password_field_tab()
    input_password_page = InputPasswordPage(browser)
    input_password_page.enter_password(valid_password)
    assert valid_password == input_password_page.check_result_text()

def test_password_field_enter_password_without_digits(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.press_password_field_tab()
    input_password_page = InputPasswordPage(browser)
    input_password_page.enter_password(password_without_digits)
    assert False == input_password_page.check_result_text_is_displayed()
    assert error_message_invalid_password == input_password_page.check_error_message_text()

def test_password_field_enter_password_without_lowercase_English_letter(browser):
    main_page = MainPage(browser)
    main_page.open_input_field_page_text_input_tab()
    input_simple_page = InputSimplePage(browser)
    input_simple_page.press_password_field_tab()
    input_password_page = InputPasswordPage(browser)
    input_password_page.enter_password(password_without_lowercase_English_letter)
    assert False == input_password_page.check_result_text_is_displayed()
    assert error_message_invalid_password == input_password_page.check_error_message_text()