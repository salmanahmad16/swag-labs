from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_page import BaseMethods

class CheckOutPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)
        self.input_first_name = (By.ID, 'first-name')
        self.input_last_name = (By.ID, 'last-name')
        self.input_postal_code = (By.ID, 'postal-code')
        self.button_continue = (By.CSS_SELECTOR, '.checkout_buttons>input')
        self.button_finish = (By.CSS_SELECTOR, '.cart_footer>a:nth-child(2)')
        self.success_meessage = (By.CLASS_NAME, 'complete-header')

    def enter_customer_details(self, fname,lname, code):
        self.base.send_values(self.input_first_name, fname)
        self.base.send_values(self.input_last_name, lname)
        self.base.send_values(self.input_postal_code, code)

    def click_on_continue(self):
        self.base.do_click(self.button_continue)

    def click_on_finish(self):
        self.base.do_click(self.button_finish)

    def verify_success_message(self):
        return self.base.get_text(self.success_meessage)

