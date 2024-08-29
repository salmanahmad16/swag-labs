import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    # Setup: Initialize the WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start the browser maximized


    # You can add more Chrome options as needed
    driver = webdriver.Chrome()

    # Return the driver to be used in tests
    yield driver

    # Teardown: Quit the WebDriver
    driver.quit()