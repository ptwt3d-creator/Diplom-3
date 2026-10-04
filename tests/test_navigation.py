import pytest
import allure
from selenium import webdriver
from pages.base_page import CommonPage


@allure.suite("UI Навигация")
@allure.sub_suite("Переходы по основным разделам шапки")
class TestNavigation:

    @allure.title("Переход из конструктора на страницу 'Лента заказов'")
    @allure.description("Проверка корректного редиректа и открытия Ленты заказов при клике на соответствующую кнопку шапки")
    def test_list_order_button_navigation(self, main_page_function_scope):
        main_page_function_scope.wait_click_list_orders_button()
        main_page_function_scope.wait_header_list_order()
    
    @allure.title("Переход из Ленты обратно в 'Конструктор'")
    @allure.description("Проверка успешного возврата на главную страницу сборки бургеров из другого раздела")
    def test_constructor_button_navigation(self, main_page_function_scope):
        main_page_function_scope.wait_click_list_orders_button()
        main_page_function_scope.wait_header_list_order()

