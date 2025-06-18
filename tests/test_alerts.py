from pages.alert_confirm_page import AlertConfirmPage
from pages.alert_page import AlertPage
from pages.alert_prompt_page import AlertPromptPage
from pages.main_page import MainPage

alert_text = 'I am an alert!'
text_for_prompt = 'Some text'
accept_result_text = 'Ok'
decline_result_text = 'Cancel'
empty_prompt_result_text = 'You entered nothing'
declined_prompt_result_text = 'You canceled the prompt'

def test_alert_box(browser):
    main_page = MainPage(browser)
    main_page.open_alert_page()
    alert_page = AlertPage(browser)
    alert_page.press_click_button()
    assert alert_text == alert_page.get_alert_text()

def test_confirmation_box_accept(browser):
    main_page = MainPage(browser)
    main_page.open_alert_page()
    alert_page = AlertPage(browser)
    alert_page.open_confirm_page()
    confirm_page = AlertConfirmPage(browser)
    confirm_page.press_click_button()
    confirm_page.confirm_alert()
    assert accept_result_text == confirm_page.check_result_text()

def test_confirmation_box_decline(browser):
    main_page = MainPage(browser)
    main_page.open_alert_page()
    alert_page = AlertPage(browser)
    alert_page.open_confirm_page()
    confirm_page = AlertConfirmPage(browser)
    confirm_page.press_click_button()
    confirm_page.decline_alert()
    assert decline_result_text == confirm_page.check_result_text()

def test_prompt_box_send_some_text(browser):
    main_page = MainPage(browser)
    main_page.open_alert_page()
    alert_page = AlertPage(browser)
    alert_page.open_prompt_page()
    prompt_page = AlertPromptPage(browser)
    prompt_page.press_click_button()
    prompt_page.send_some_text_in_prompt(text_for_prompt)
    assert text_for_prompt == prompt_page.check_result_text()

def test_prompt_box_accept_without_text(browser):
    main_page = MainPage(browser)
    main_page.open_alert_page()
    alert_page = AlertPage(browser)
    alert_page.open_prompt_page()
    prompt_page = AlertPromptPage(browser)
    prompt_page.press_click_button()
    prompt_page.send_some_text_in_prompt()
    assert empty_prompt_result_text == prompt_page.check_result_text()

def test_prompt_box_decline(browser):
    main_page = MainPage(browser)
    main_page.open_alert_page()
    alert_page = AlertPage(browser)
    alert_page.open_prompt_page()
    prompt_page = AlertPromptPage(browser)
    prompt_page.press_click_button()
    prompt_page.decline_prompt()
    assert declined_prompt_result_text == prompt_page.check_result_text()
