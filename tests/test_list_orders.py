import pytest
import allure
from pages.list_order_page import OrderPage
from pages.main_page import MainPage


@allure.suite("UI Лента заказов")
@allure.sub_suite("Проверка счетчиков и списков заказов")
class TestListOrder:

    @allure.title("Увеличение счетчика ингредиента при добавлении в конструктор")
    @allure.description("Проверка, что при перетаскивании ингредиента в зону сборки его счетчик становится равен 1")
    def test_counter_ingredient(self, main_page_function_scope):
        main_page_function_scope.drag_and_drop_ingedient_to_choose_area()
        main_page_function_scope.wait_counter_ingredient_1()

        assert main_page_function_scope.get_ingredient_counter_value() == "1"

    @allure.title("Увеличение счетчика 'Выполнено за все время' при создании заказа")
    @allure.description("Проверка, что после оформления заказа под авторизованным пользователем общий счетчик увеличивается на 1")
    def test_counter_all_time_increased(self, login_page_function_scope):
        main_page = MainPage(login_page_function_scope.driver) # login_page_function_scope и подобные - объекты классов и имеют конструктор driver наследуемый от Basepage, driver задается в фикстурах
        list_order_page = OrderPage(login_page_function_scope.driver)

        login_page_function_scope.login_on_site()
        login_page_function_scope.wait_invisibility_modal_overlay()

        main_page.wait_header_collect_burger()
        list_order_page.wait_click_list_orders_button()
        list_order_page.wait_header_list_order()

        counter_all_time_value = list_order_page.get_value_counter_all_time()

        list_order_page.wait_click_constructor_button()
        
        main_page.wait_header_collect_burger()
        main_page.drag_and_drop_bun_to_choose_area()
        main_page.wait_click_create_order_button()
        main_page.wait_click_close_window_order_created()

        # Переход на страницу списка заказов для просмотра счетчика заказов 
        main_page.js_wait_click_list_order_button()

        # Запись в переменную значения счетчика после создания заказа
        counter_all_time_value_increased = list_order_page.get_value_counter_all_time()

        assert int(counter_all_time_value_increased) == int(counter_all_time_value) + 1

    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при создании заказа")
    @allure.description("Проверка, что после оформления заказа под авторизованным пользователем ежедневный счетчик увеличивается на 1")
    def test_counter_to_day_increased(self, login_page_function_scope):
        main_page = MainPage(login_page_function_scope.driver)
        list_order_page = OrderPage(login_page_function_scope.driver)

        login_page_function_scope.login_on_site()
        login_page_function_scope.wait_invisibility_modal_overlay()

        main_page.wait_header_collect_burger()
        list_order_page.wait_click_list_orders_button()
        list_order_page.wait_header_list_order()

        counter_to_day_value = list_order_page.get_value_counter_to_day()

        list_order_page.wait_click_constructor_button()
        
        main_page.wait_header_collect_burger()
        main_page.drag_and_drop_bun_to_choose_area()
        main_page.wait_click_create_order_button()
        main_page.wait_click_close_window_order_created()
        
        # Переход на страницу списка заказов для просмотра счетчика заказов 
        main_page.js_wait_click_list_order_button()
        
        # Запись в переменную значения счетчика после создания заказа
        counter_to_day_value_increased = list_order_page.get_value_counter_to_day()

        assert int(counter_to_day_value_increased) == int(counter_to_day_value) + 1
    
    @allure.title("Отображение номера созданного заказа в блоке 'В работе'")
    @allure.description("Проверка, что номер только что созданного заказа появляется в списке активных заказов в Ленте")
    def test_check_created_number_order_in_work_list(self, login_page_function_scope):
        main_page = MainPage(login_page_function_scope.driver)
        list_order_page = OrderPage(login_page_function_scope.driver)

        login_page_function_scope.login_on_site()
        login_page_function_scope.wait_invisibility_modal_overlay()

        main_page.wait_header_collect_burger()
        main_page.drag_and_drop_bun_to_choose_area()
        main_page.wait_click_create_order_button()
        main_page.wait_ready_window_order_created()

        # Сохраняем номер созданного заказа
        num_order_window = main_page.get_number_oreder_in_window_created_order()
        
        main_page.js_click_close_button_oreder_created()
        main_page.js_wait_click_list_order_button()
        list_order_page.wait_header_list_order()

        # Ожидаем появления номера заказа на странице списка заказов
        list_order_page.wait_number_order_in_work_list(num_order_window)

        # Сохраняем в переменную для последующего сравнения с номером заказа полученым при создании заказа
        num_order_work_list = list_order_page.get_number_oreder_in_list_work()

        assert "0"+str(num_order_window) in str(num_order_work_list)

