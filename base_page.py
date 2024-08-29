from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import re

class BaseMethods:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(locator)).click()
        except:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(locator)).click()

    def send_values(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).clear()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)).text

    def get_all_elements(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located(locator))