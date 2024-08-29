import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_page import BaseMethods

class ProductListingPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)
        self.all_item_names = (By.CLASS_NAME, 'inventory_item_name')


    def select_item(self, name):
        all_items = self.base.get_all_elements(self.all_item_names)
        for item in all_items:
            time.sleep(1)
            if item.text == name:
                time.sleep(1)
                item.click()
                break