import time

from pages.login_page import LoginPage


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.click_form_authentication()
    login_page.type_username('test')
    login_page.type_password('123')
    login_page.click_login_button()

