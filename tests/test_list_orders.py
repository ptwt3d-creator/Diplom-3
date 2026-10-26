import pytest
import allure
from selenium import webdriver
from pages.list_order_page import OrderPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.suite("UI Лента заказов")
@allure.sub_suite("Проверка счетчиков и списков заказов")
class TestListOrder:

    @allure.title("Увеличение счетчика ингредиента при добавлении в конструктор")
    @allure.description("Проверка, что при перетаскивании ингредиента в зону сборки его счетчик становится равен 1")
    def test_counter_ingredient(self, main_page_function_scope):
        main_page_function_scope.drag_and_drop_ingedient_to_choose_area()
        main_page_function_scope.wait_counter_ingredient_1()

    @allure.title("Увеличение счетчика 'Выполнено за все время' при создании заказа")
    @allure.description("Проверка, что после оформления заказа под авторизованным пользователем общий счетчик увеличивается на 1")
    def test_counter_all_time_increased(self, driver_function_scope, login_page_function_scope):
        main_page = MainPage(driver_function_scope)
        list_order = OrderPage(driver_function_scope)

        login_page_function_scope.login_on_site()
        login_page_function_scope.wait_invisibility_modal_overlay()

        main_page.wait_header_collect_burger()
        list_order.wait_click_list_orders_button()


        counter_all_time_value = list_order.get_value_counter_all_time()
        list_order.wait_click_constructor_button()
        main_page.wait_header_collect_burger()
        main_page.drag_and_drop_bun_to_choose_area()
        main_page.wait_click_create_order_button()
        main_page.wait_click_close_window_order_created()
        main_page.js_wait_click_list_order_button()
    
        counter_all_time_value_increased = list_order.get_value_counter_all_time()

        assert int(counter_all_time_value_increased) == int(counter_all_time_value) + 1

    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при создании заказа")
    @allure.description("Проверка, что после оформления заказа под авторизованным пользователем ежедневный счетчик увеличивается на 1")
    def test_counter_to_day_increased(self, driver_function_scope, login_page_function_scope):
        main_page = MainPage(driver_function_scope)
        list_order = OrderPage(driver_function_scope)

        login_page_function_scope.login_on_site()
        login_page_function_scope.wait_invisibility_modal_overlay()

        main_page.wait_header_collect_burger()
        list_order.wait_click_list_orders_button()


        counter_to_day_value = list_order.get_value_counter_to_day()
        list_order.wait_click_constructor_button()
        main_page.wait_header_collect_burger()
        main_page.drag_and_drop_bun_to_choose_area()
        main_page.wait_click_create_order_button()
        main_page.wait_click_close_window_order_created()
        main_page.js_wait_click_list_order_button()
    
        counter_to_day_value_increased = list_order.get_value_counter_to_day()

        assert int(counter_to_day_value_increased) == int(counter_to_day_value) + 1
    
    @allure.title("Отображение номера созданного заказа в блоке 'В работе'")
    @allure.description("Проверка, что номер только что созданного заказа появляется в списке активных заказов в Ленте")
    def test_check_created_number_order_in_work_list(self, driver_function_scope, login_page_function_scope):
        main_page = MainPage(driver_function_scope)
        list_order = OrderPage(driver_function_scope)

        login_page_function_scope.login_on_site()
        login_page_function_scope.wait_invisibility_modal_overlay()

        main_page.wait_header_collect_burger()
        main_page.drag_and_drop_bun_to_choose_area()
        main_page.wait_click_create_order_button()

        main_page.wait_ready_window_order_created()
        num_order_window = main_page.get_number_oreder_in_window_created_order()
        main_page.js_click_close_button_oreder_created()
        main_page.js_wait_click_list_order_button()

        list_order.wait_header_list_order
        list_order.wait_number_order_in_work_list(num_order_window)
        num_order_work_list = list_order.get_number_oreder_in_list_work()
    
        counter_to_day_value_increased = list_order.get_value_counter_to_day()

        assert "0"+str(num_order_window) in str(num_order_work_list)

