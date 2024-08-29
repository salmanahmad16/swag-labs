import time
import configparser
from itertools import product

import pytest
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage

config = configparser.ConfigParser()
config.read('config.ini')


username = config['credentials']['username']
password = config['credentials']['password']

product_name = "Sauce Labs Backpack"
product_price = '$29.99'

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    pl_page = ProductListingPage(driver)
    dp_page = ProductDetailPage(driver)
    c_page = CartPage(driver)
    co_page = CheckOutPage(driver)

    login_page.load()           # Load Url
    login_page.enter_user_name(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    verify = login_page.verify_login()  # Verify Login
    assert 'Products' in verify

    pl_page.select_item(product_name)   # Select the Product By Name
    verify_price = dp_page.verify_item_price(product_price)
    assert product_price in verify_price    # Verify Correct product is selected

    dp_page.add_to_cart()       # Adding product into cart
    dp_page.view_cart()         # Go to Cart

    verify_item_name = c_page.verify_item_name()
    assert product_name in verify_item_name     # Verify the product name on the Cart Page

    verify_item_price = c_page.verify_item_price()
    assert '29.99' in verify_item_price         # Verify the product price in the Cart Page

    c_page.go_to_checkout()
    co_page.enter_customer_details("Leo2", "Khan", "9988")
    co_page.click_on_continue()
    co_page.click_on_finish()
    success_msg = co_page.verify_success_message()
    assert 'THANK YOU FOR YOUR ORDER' in success_msg
    time.sleep(2)
