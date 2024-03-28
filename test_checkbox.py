from pages.checkbox import CheckBox

def test_checkbox(driver):
    checkbox = CheckBox(driver)
    checkbox.click_checkbox_link()
    checkbox.click_checkbox()
