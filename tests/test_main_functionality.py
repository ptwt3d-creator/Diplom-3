import pytest
import allure


@allure.suite("UI Главный функционал")
@allure.sub_suite("Модальное окно деталей ингредиента")
class TestMainFunc:

    @allure.title("Открытие модального окна с деталями ингредиента")
    @allure.description("Проверка, что при клике на карточку ингредиента всплывает окно с его подробным описанием")
    def test_open_details(self, main_page_function_scope):
        main_page_function_scope.wait_click_ingredient()
        main_page_function_scope.wait_window_details()

        assert main_page_function_scope.is_window_details_displayed()
    
    @allure.title("Закрытие модального окна деталей ингредиента")
    @allure.description("Проверка, что при нажатии на крестик окно деталей успешно закрывается и исчезает с экрана")
    def test_close_detals(self, main_page_function_scope):
        main_page_function_scope.wait_click_ingredient()
        main_page_function_scope.wait_window_details()
        main_page_function_scope.wait_click_close_details_button()
        main_page_function_scope.wait_close_details()

        assert main_page_function_scope.is_window_details_invisibility()

    

    