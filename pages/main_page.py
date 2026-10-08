from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators.main_page_locators import Locators
from pages.base_page import CommonPage

class MainPage(CommonPage):
    
    def __init__(self, driver):
        self.driver = driver

    def wait_click_ingredient(self):
        element = self.wait_for_element_clickable(Locators.INGRIDIENT)
        element.click()
    
    def wait_window_details(self):
        self.wait_for_element_visible(Locators.HEADER_INGREDIENT_DETALS)

    def wait_click_close_details_button(self):
        element = self.wait_for_element_clickable(Locators.BUTTON_CLOSE_DETAILS)
        element.click()

    def wait_close_details(self):
        self.wait_for_element_invisibility(Locators.HEADER_INGREDIENT_DETALS)
    
    def drag_and_drop_ingedient_to_choose_area(self):
        self.drag_and_drop_element(Locators.INGRIDIENT, Locators.BASKET_INGREDIENTS)

    def check_counter_ingredient_1(self):
        self.wait_text_in_element(Locators.COUNTER_INGRIDIENT, "1")
    
    def drag_and_drop_bun_to_choose_area(self):
        self.drag_and_drop_element(Locators.BUN, Locators.BASKET_INGREDIENTS)

    def wait_click_create_order_button(self):
        element = self.wait_for_element_clickable(Locators.ORDER_CREATE_BUTTON)
        element.click()
    
    def wait_click_close_window_order_created(self):
        element = self.wait_for_element_visable(Locators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
        element.click()
        
    def wait_header_collect_burger(self):
        self.wait_for_element_visible(Locators.HEADER_COLLECT_BURGER)
    
    def js_wait_click_button_close_creted_order(self):
        self.js_wait_click(Locators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    
    def wait_click_close_window_order_created(self):
        self.wait_text_not_in_element_list_variants(Locators.NUMBER_ORDER_IN_ORDER_CREATED, ["9999", "999", ""])
        self.js_wait_click(Locators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    
    def get_number_oreder_in_window_created_order(self):
        return self.find_element(Locators.NUMBER_ORDER_IN_ORDER_CREATED).text
    
    def wait_ready_window_order_created(self):
        self.wait_text_not_in_element_list_variants(Locators.NUMBER_ORDER_IN_ORDER_CREATED, ["9999", "999", ""])

    def js_click_close_button_oreder_created(self):
        self.js_wait_click(Locators.BUTTON_CLOSE_WINDOW_ORDER_CREATED)
    