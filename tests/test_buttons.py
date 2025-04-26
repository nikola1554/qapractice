from pages.disabled_page import DisabledPage
from pages.like_a_button_page import LikeAButtonPage
from pages.main_page import MainPage
from pages.buttons_page import ButtonsPage

def test_click_button_simple_button_tab(browser):
    main_page = MainPage(browser)
    main_page.open_buttons_page()
    buttons_page = ButtonsPage(browser)
    assert buttons_page.click_button_is_displayed()
    assert 'Click' == buttons_page.check_label_click_button()
    buttons_page.press_click_button()
    assert 'Submitted' == buttons_page.check_result_text()

def test_click_button_like_a_button_tab(browser):
    main_page = MainPage(browser)
    main_page.open_buttons_page()
    buttons_page = ButtonsPage(browser)
    buttons_page.press_looks_like_a_button_tab()
    like_a_button_page = LikeAButtonPage(browser)
    assert like_a_button_page.click_button_is_displayed()
    assert 'Click' == like_a_button_page.check_text_click_button()
    like_a_button_page.press_click_button()
    assert 'Submitted' == like_a_button_page.check_result_text()

def test_click_button_disabled_tab(browser):
    main_page = MainPage(browser)
    main_page.open_buttons_page()
    buttons_page = ButtonsPage(browser)
    buttons_page.press_disabled_tab()
    disabled_page = DisabledPage(browser)
    assert not disabled_page.check_state_submit_button()
    disabled_page.switch_to_enabled_state_drop_down()
    assert disabled_page.check_state_submit_button()
    disabled_page.switch_to_disabled_state_drop_down()
    assert not disabled_page.check_state_submit_button()
    disabled_page.switch_to_enabled_state_drop_down()
    disabled_page.press_submit_button()
    assert 'Submitted' == disabled_page.check_result_text()

