from selenium.webdriver.common.by import By


class LoginPageLocators:
    MAKE_APPOINTMENT_BUTTON = (By.XPATH, "//a[@id='btn-make-appointment']")
    User_Name = (By.XPATH, "//input[@id='txt-username']")
    Pass_Word = (By.XPATH, "//input[@id='txt-password']")
    Submit = (By.XPATH, "//button[@id='btn-login']")

