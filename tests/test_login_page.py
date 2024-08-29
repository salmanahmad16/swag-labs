import time
import configparser
import pytest
from pages.login_page import LoginPage

config = configparser.ConfigParser()
config.read('config.ini')


username = config['credentials']['username']
password = config['credentials']['password']

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_user_name(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    verify = login_page.verify_login()
    assert 'Products' in verify

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_user_name("abc")
    login_page.enter_password("password")
    login_page.click_login_button()
    error_message = login_page.verify_error_message()
    assert 'Epic sadface: Username and password do not match any user in this service' in error_message



