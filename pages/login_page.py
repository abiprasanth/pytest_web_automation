from selenium.webdriver.common.by import By
from pages.common import CommonOps


class LoginPage(CommonOps):
    FORM_AUTHENTICATION_LINK = (By.LINK_TEXT, 'Form Authentication')
    USERNAME_TEXTBOX = (By.ID, 'username')
    PASSWORD_TEXTBOX = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')

    def click_form_authentication(self):
        self.wait_for(self.FORM_AUTHENTICATION_LINK).click()

    def type_username(self, username):
        self.wait_for(self.USERNAME_TEXTBOX).send_keys(username)

    def type_password(self, password):
        self.wait_for(self.PASSWORD_TEXTBOX).send_keys(password)

    def click_login_button(self):
        self.wait_for(self.LOGIN_BUTTON).click()
