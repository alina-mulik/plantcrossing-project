import pytest
import time
from selenium import webdriver



@pytest.yield_fixture(scope="function", autouse=True)
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")

    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)

    try:
        yield browser
    finally:
        browser.close()
        browser.quit()