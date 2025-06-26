from pages.iframe_iframe_page import IframePage
from pages.main_page import MainPage
import time

iframe_page_title_text = 'Album example'
main_page_title_text = 'Iframes'

def test_switching_to_iframe_and_back(browser):
    main_page = MainPage(browser)
    main_page.open_iframe_page()
    iframe_page = IframePage(browser)
    iframe_page.switch_to_iframe_page()
    assert iframe_page_title_text == iframe_page.check_title_iframe_page()
    iframe_page.switch_to_main_page()
    assert main_page_title_text == iframe_page.check_title_main_page()