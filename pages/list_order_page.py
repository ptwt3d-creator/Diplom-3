from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators.list_order_page_locators import Locators
from pages.base_page import CommonPage

class OrderPage(CommonPage):
    
    def get_value_counter_all_time(self):
        return self.get_text_from_element(Locators.COUNTER_ORDERS_COMLITE_ALL_TIME)
    
    def get_value_counter_to_day(self):
        return self.get_text_from_element(Locators.COUNTER_ORDERS_COMLITE_TO_DAY)
    
    def get_number_oreder_in_list_work(self):
        return self.get_text_from_element(Locators.LIST_ORDER_IN_WORK)

    def wait_number_order_in_work_list(self, number):
        WebDriverWait(self.driver, 10).until(
            lambda driver: number in driver.find_element(*Locators.LIST_ORDER_IN_WORK).text
        )