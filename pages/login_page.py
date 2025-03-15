from selenium import webdriver
from locators.login_page_locators import LoginPageLocators
from utils.config import BASE_URL


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def click_make_apt(self):
        self.driver.find_element(*LoginPageLocators.MAKE_APPOINTMENT_BUTTON).click()

    def user_name(self):
        self.driver.find_element(*LoginPageLocators.User_Name).send_keys('John Doe')

    def password(self):
        self.driver.find_element(*LoginPageLocators.Pass_Word).send_keys('ThisIsNotAPassword')

    def submit(self):
        self.driver.find_element(*LoginPageLocators.Submit).click()
