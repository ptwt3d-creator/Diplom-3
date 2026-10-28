from locators.main_page_locators import MainLocators
from pages.base_page import CommonPage
import allure


class MainPage(CommonPage):
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по ингредиенту")
    def wait_click_ingredient(self):
        element = self.wait_for_element_clickable(MainLocators.INGRIDIENT)
        element.click()
    
    @allure.step("Ожидание открытия окна с деталями ингредиента")
    def wait_window_details(self):
        self.wait_for_element_visible(MainLocators.HEADER_INGREDIENT_DETALS)
    
    @allure.step("Запрос статуса видимости окна деталей")
    def is_window_details_displayed(self):
        return self.find_element(MainLocators.HEADER_INGREDIENT_DETALS).is_displayed() # is_displayed() проверяет виден ли элемент на экране, поверяет по DOM-дереву так что оверлеи ему не мешают

    @allure.step("Ожидание закрытия (невидимости) окна с деталями")
    def is_window_details_invisibility(self):
        return self.wait_for_element_invisibility(MainLocators.HEADER_INGREDIENT_DETALS)
    
    @allure.step("Клик по кнопке закрытия деталей")
    def wait_click_close_details_button(self):
        element = self.wait_for_element_clickable(MainLocators.BUTTON_CLOSE_DETAILS)
        element.click()

    @allure.step("Ожидание скрытия деталей ингредиента")
    def wait_close_details(self):
        self.wait_for_element_invisibility(MainLocators.HEADER_INGREDIENT_DETALS)
    
    @allure.step("Перетаскивание ингредиента в область заказа")
    def drag_and_drop_ingedient_to_choose_area(self):
        self.drag_and_drop_element(MainLocators.INGRIDIENT, MainLocators.BASKET_INGREDIENTS)

    @allure.step("Ожидание, пока счетчик ингредиента станет равен '1'")
    def wait_counter_ingredient_1(self):
        self.wait_text_in_element(MainLocators.COUNTER_INGRIDIENT, "1")
    
    @allure.step("Перетаскивание булки в область заказа")
    def drag_and_drop_bun_to_choose_area(self):
        self.drag_and_drop_element(MainLocators.BUN, MainLocators.BASKET_INGREDIENTS)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def wait_click_create_order_button(self):
        element = self.wait_for_element_clickable(MainLocators.ORDER_CREATE_BUTTON)
        element.click()

    @allure.step("Ожидание появления заголовка 'Соберите бургер'")
    def wait_header_collect_burger(self):
        self.wait_for_element_visible(MainLocators.HEADER_COLLECT_BURGER)
    
    @allure.step("JS-ожидание и клик закрытия окна созданного заказа")
    def js_wait_click_button_close_creted_order(self):
        self.js_wait_click(MainLocators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    
    @allure.step("Ожидание создания и закрытие окна созданного заказа")
    def wait_click_close_window_order_created(self):
        self.wait_text_not_in_element_list_variants(MainLocators.NUMBER_ORDER_IN_ORDER_CREATED, ["9999", "999", ""])
        self.js_wait_click(MainLocators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    
    @allure.step("Получение номера созданного заказа из окна заказ создан")
    def get_number_oreder_in_window_created_order(self):
        return self.find_element(MainLocators.NUMBER_ORDER_IN_ORDER_CREATED).text
    
    @allure.step("Ожидание загрузки и готовности окна созданного заказа")
    def wait_ready_window_order_created(self):
        self.wait_text_not_in_element_list_variants(MainLocators.NUMBER_ORDER_IN_ORDER_CREATED, ["9999", "999", ""])

    @allure.step("JS-клик по кнопке закрытия созданного заказа")
    def js_wait_click_close_button_oreder_created(self):
        self.js_wait_click(MainLocators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    
    @allure.step("Получение текущего значения счетчика ингредиента")
    def get_ingredient_counter_value(self):
        value = self.find_element(MainLocators.COUNTER_INGRIDIENT).text
        return str(value)