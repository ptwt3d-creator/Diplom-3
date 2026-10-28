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

        with allure.step("Проверка, что окно с деталями ингредиента отображается на экране"):
            assert main_page_function_scope.is_window_details_displayed()
    
    @allure.title("Закрытие модального окна деталей ингредиента")
    @allure.description("Проверка, что при нажатии на крестик окно деталей успешно закрывается и исчезает с экрана")
    def test_close_detals(self, main_page_function_scope):
        main_page_function_scope.wait_click_ingredient()
        main_page_function_scope.wait_window_details()
        main_page_function_scope.wait_click_close_details_button()
        main_page_function_scope.wait_close_details()

        with allure.step("Проверка, что окно деталей ингредиента закрылось и стало невидимым"):
            assert main_page_function_scope.is_window_details_invisibility()
    
    @allure.title("Увеличение счетчика ингредиента при добавлении в конструктор")
    @allure.description("Проверка, что при перетаскивании ингредиента в зону сборки его счетчик становится равен 1")
    def test_counter_ingredient(self, main_page_function_scope):
        main_page_function_scope.drag_and_drop_ingedient_to_choose_area()
        main_page_function_scope.wait_counter_ingredient_1()

        with allure.step("Проверка, что значение счетчика ингредиента стало равно '1'"):
            assert main_page_function_scope.get_ingredient_counter_value() == "1"

    

    