import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    url = "https://the-internet.herokuapp.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.close()
