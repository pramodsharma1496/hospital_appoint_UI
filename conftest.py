from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

from venv.bin import pytest


@pytest.fixture(scope="function")
def browser():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
