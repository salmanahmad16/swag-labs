from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_page import BaseMethods

class ProductDetailPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)
        self.price= (By.CLASS_NAME, 'inventory_details_price')
        self.button_add_to_cart = (By.CSS_SELECTOR, 'button.btn_inventory')
        self.button_view_cart = (By.CSS_SELECTOR, '.shopping_cart_container>a')

    def verify_item_price(self, price):
        return self.base.get_text(self.price)

    def add_to_cart(self):
        self.base.do_click(self.button_add_to_cart)

    def view_cart(self):
        self.base.do_click(self.button_view_cart)




