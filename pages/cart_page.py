from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_page import BaseMethods

class CartPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)
        self.item_name = (By.CLASS_NAME, 'inventory_item_name')
        self.item_price = (By.CLASS_NAME, 'inventory_item_price')
        self.button_checkout = (By.CSS_SELECTOR, '.cart_footer>a:nth-child(2)')

    def verify_item_name(self):
        return self.base.get_text(self.item_name)

    def verify_item_price(self):
        return self.base.get_text(self.item_price)

    def go_to_checkout(self):
        self.base.do_click(self.button_checkout)

