import pytest
from selenium import webdriver
from pages.login_page import LoginPage


def test_make_appointment():
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_make_apt()

    assert "Login" in driver.page_source
    login_page.user_name()
    login_page.password()
    login_page.submit()
    driver.quit()
