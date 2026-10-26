import pytest
from selenium import webdriver
from data import Urls
from pages.main_page import MainPage
from pages.list_order_page import OrderPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture()
def main_page_function_scope(driver):
    driver.get(Urls.MAIN_PAGE_STELLAR)
    return MainPage(driver)

@pytest.fixture()
def list_order_page_function_scope(driver):
    driver.get(Urls.LIST_ORDERS_STELLAR)
    return OrderPage(driver)

@pytest.fixture()
def login_page_function_scope(driver):
    driver.get(Urls.LOGIN)
    return LoginPage(driver)
