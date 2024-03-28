from pages.common import CommonOps
from selenium.webdriver.common.by import By

class CheckBox(CommonOps):
    CHECKBOX = (By.LINK_TEXT, 'Checkboxes')
    BOX_2 = (By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')

    def click_checkbox_link(self):
        self.wait_for(self.CHECKBOX).click()

    def click_checkbox(self):
        self.wait_for(self.BOX_2).click()