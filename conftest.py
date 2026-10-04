import pytest
from selenium import webdriver
from data import Urls
from pages.base_page import CommonPage
from pages.main_page import MainPage
from pages.list_order_page import OrderPage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def driver_function_scope():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture()
def main_page_function_scope(driver_function_scope):
    driver_function_scope.get(Urls.MAIN_PAGE_STELLAR)
    return MainPage(driver_function_scope)

@pytest.fixture()
def list_order_page_function_scope(driver_function_scope):
    driver_function_scope.get(Urls.LIST_ORDERS_STELLAR)
    return OrderPage(driver_function_scope)

@pytest.fixture()
def login_page_function_scope(driver_function_scope):
    driver_function_scope.get(Urls.LOGIN)
    return LoginPage(driver_function_scope)
