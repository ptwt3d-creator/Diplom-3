import pytest
import allure
from pages.list_order_page import OrderPage
from pages.main_page import MainPage
from data import Urls


@allure.suite("UI Навигация")
@allure.sub_suite("Переходы по основным разделам шапки")
class TestNavigation:

    @allure.title("Переход из конструктора на страницу 'Лента заказов'")
    @allure.description("Проверка открытия Ленты заказов при клике на соответствующую кнопку шапки")
    def test_list_order_button_navigation(self, main_page_function_scope):
    
        main_page_function_scope.wait_click_list_orders_button() # клик по кнопке список заказов - переход на страницу списка заказов с главной страницы бургерной

        # (ждем не url а заголовок страницы чтобы убедится что страница тоже загрузилась)
        list_order_page = OrderPage(main_page_function_scope.driver) # Создаем объект list_order_page на основе запущенного драйвера(уже открытой страницы браузера) для использоваиня методов страницы списка заказов (https://qa-stellarburgers.education-services.ru/feed) и не создания еще одного драйвера(еще одно открытие страницы браузера нам не нужно уже был открыт ранее фикстурой main_page_function_scope в открытом браузере и нужно работать)
        list_order_page.wait_header_list_order() # через созданный объект страницы списка заказов, использем методы этой страницы, всё в одном драйвере, который создался при инициализации теста через main_page_function_scope

        with allure.step(f"Проверка, что текущий URL соответствует странице Ленты заказов: {Urls.LIST_ORDERS_STELLAR}"):
            assert list_order_page.get_current_url() == Urls.LIST_ORDERS_STELLAR

    
    @allure.title("Переход из Ленты в 'Конструктор'")
    @allure.description("Проверка возврата на главную страницу сборки бургеров из другого раздела")
    def test_constructor_button_navigation(self, list_order_page_function_scope):

        list_order_page_function_scope.wait_click_constructor_button()

        main_page = MainPage(list_order_page_function_scope.driver)
        main_page.wait_header_collect_burger()
        
        with allure.step(f"Проверка, что текущий URL соответствует главной странице Конструктора: {Urls.MAIN_PAGE_STELLAR}"):
            assert main_page.get_current_url() == Urls.MAIN_PAGE_STELLAR

