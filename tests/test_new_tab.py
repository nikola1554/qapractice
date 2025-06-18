from pages.new_tab_button_page import NewTabButtonPage
from pages.new_tab_link_page import NewTabLinkPage
from pages.main_page import MainPage
import time
from pages.new_tab_new_page_page import NewTabNewPagePage

result_text = 'I am a new page in a new tab'

def test_new_tab_link(browser):
    main_page = MainPage(browser)
    main_page.open_new_tab_link_page()
    new_tab_link_page = NewTabLinkPage(browser)
    new_tab_link_page.click_link_new_tab_new_page()
    new_tab_new_page_page = NewTabNewPagePage(browser)
    assert '/new_tab/new_page' in new_tab_new_page_page.check_url()
    assert result_text == new_tab_new_page_page.check_result_text()

def test_new_tab_link_missing_result_text(browser):
    main_page = MainPage(browser)
    main_page.open_new_tab_link_page()
    new_tab_link_page = NewTabLinkPage(browser)
    new_tab_link_page.click_link_new_tab_new_page()
    new_tab_new_page_page = NewTabNewPagePage(browser)
    new_tab_new_page_page.switch_to_previous_tab()
    assert '/new_tab/new_page'not in new_tab_link_page.check_url()
    assert not new_tab_link_page.check_result_text_is_displayed()

def test_new_tab_button(browser):
    main_page = MainPage(browser)
    main_page.open_new_tab_link_page()
    new_tab_link_page = NewTabLinkPage(browser)
    new_tab_link_page.open_new_tab_button_page()
    new_tab_button_page = NewTabButtonPage(browser)
    new_tab_button_page.click_button_new_tab_new_page()
    new_tab_new_page_page = NewTabNewPagePage(browser)
    assert '/new_tab/new_page' in new_tab_new_page_page.check_url()
    assert result_text == new_tab_new_page_page.check_result_text()

def test_new_tab_button_missing_result_text(browser):
    main_page = MainPage(browser)
    main_page.open_new_tab_link_page()
    new_tab_link_page = NewTabLinkPage(browser)
    new_tab_link_page.open_new_tab_button_page()
    new_tab_button_page = NewTabButtonPage(browser)
    new_tab_button_page.click_button_new_tab_new_page()
    new_tab_new_page_page = NewTabNewPagePage(browser)
    new_tab_new_page_page.switch_to_previous_tab()
    assert '/new_tab/new_page'not in new_tab_link_page.check_url()
    assert not new_tab_link_page.check_result_text_is_displayed()
