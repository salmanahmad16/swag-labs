from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_page import BaseMethods

class LoginPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)
        self.url = "https://www.saucedemo.com/v1/index.html"
        self.field_user_name = (By.ID, 'user-name')
        self.field_password = (By.ID, 'password')
        self.button_login = (By.ID, 'login-button')
        self.error_message = (By.TAG_NAME, 'h3')
        self.text_product = (By.CLASS_NAME, 'product_label')

    def load(self):
        self.driver.get(self.url)

    def enter_user_name(self, name):
        self.base.send_values(self.field_user_name, name)

    def enter_password(self,password):
        self.base.send_values(self.field_password, password)

    def click_login_button(self):
        self.base.do_click(self.button_login)

    def verify_login(self):
        return self.base.get_text(self.text_product)

    def verify_error_message(self):
        return self.base.get_text(self.error_message)


