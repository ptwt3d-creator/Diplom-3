import pytest
import allure
from selenium import webdriver
from data import Urls
from pages.main_page import MainPage
from pages.list_order_page import OrderPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    with allure.step("Запуск браузера Chrome"):
        browser = webdriver.Chrome()
    yield browser
    with allure.step("Закрытие браузера"):
        browser.quit()

@pytest.fixture()
def main_page_function_scope(driver):
    with allure.step(f"Переход на главную страницу: {Urls.MAIN_PAGE_STELLAR}"):
        driver.get(Urls.MAIN_PAGE_STELLAR)
    return MainPage(driver)

@pytest.fixture()
def list_order_page_function_scope(driver):
    with allure.step(f"Переход на страницу ленты заказов: {Urls.LIST_ORDERS_STELLAR}"):
        driver.get(Urls.LIST_ORDERS_STELLAR)
    return OrderPage(driver)

@pytest.fixture()
def login_page_function_scope(driver):
    with allure.step(f"Переход на страницу авторизации: {Urls.LOGIN}"):
        driver.get(Urls.LOGIN)
    return LoginPage(driver)

