from locators.main_page_locators import MainLocators
from pages.base_page import CommonPage

class MainPage(CommonPage):
    
    def __init__(self, driver):
        self.driver = driver

    def wait_click_ingredient(self):
        element = self.wait_for_element_clickable(MainLocators.INGRIDIENT)
        element.click()
    
    def wait_window_details(self):
        self.wait_for_element_visible(MainLocators.HEADER_INGREDIENT_DETALS)
    
    def is_window_details_displayed(self):
        return self.find_element(MainLocators.HEADER_INGREDIENT_DETALS).is_displayed() # is_displayed() проверяет виден ли элемент на экране, поверяет по DOM-дереву так что оверлеи ему не мешают

    def is_window_details_invisibility(self):
        return self.wait_for_element_invisibility(MainLocators.HEADER_INGREDIENT_DETALS)
    
    def wait_click_close_details_button(self):
        element = self.wait_for_element_clickable(MainLocators.BUTTON_CLOSE_DETAILS)
        element.click()

    def wait_close_details(self):
        self.wait_for_element_invisibility(MainLocators.HEADER_INGREDIENT_DETALS)
    
    def drag_and_drop_ingedient_to_choose_area(self):
        self.drag_and_drop_element(MainLocators.INGRIDIENT, MainLocators.BASKET_INGREDIENTS)

    def wait_counter_ingredient_1(self):
        self.wait_text_in_element(MainLocators.COUNTER_INGRIDIENT, "1")
    
    def drag_and_drop_bun_to_choose_area(self):
        self.drag_and_drop_element(MainLocators.BUN, MainLocators.BASKET_INGREDIENTS)

    def wait_click_create_order_button(self):
        element = self.wait_for_element_clickable(MainLocators.ORDER_CREATE_BUTTON)
        element.click()

    def wait_header_collect_burger(self):
        self.wait_for_element_visible(MainLocators.HEADER_COLLECT_BURGER)
    
    def js_wait_click_button_close_creted_order(self):
        self.js_wait_click(MainLocators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    
    def wait_click_close_window_order_created(self):
        self.wait_text_not_in_element_list_variants(MainLocators.NUMBER_ORDER_IN_ORDER_CREATED, ["9999", "999", ""])
        self.js_wait_click(MainLocators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    
    def get_number_oreder_in_window_created_order(self):
        return self.find_element(MainLocators.NUMBER_ORDER_IN_ORDER_CREATED).text
    
    def wait_ready_window_order_created(self):
        self.wait_text_not_in_element_list_variants(MainLocators.NUMBER_ORDER_IN_ORDER_CREATED, ["9999", "999", ""])

    def js_click_close_button_oreder_created(self):
        self.js_wait_click(MainLocators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    
    def get_ingredient_counter_value(self):
        value = self.find_element(MainLocators.COUNTER_INGRIDIENT).text
        return str(value)