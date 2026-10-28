from locators.list_order_page_locators import OrderLocators
from pages.base_page import CommonPage

class OrderPage(CommonPage):
    
    def get_value_counter_all_time(self):
        return self.get_text_from_element(OrderLocators.COUNTER_ORDERS_COMLITE_ALL_TIME)
    
    def get_value_counter_to_day(self):
        return self.get_text_from_element(OrderLocators.COUNTER_ORDERS_COMLITE_TO_DAY)
    
    def get_number_oreder_in_list_work(self):
        return self.get_text_from_element(OrderLocators.LIST_ORDER_IN_WORK)

    def wait_number_order_in_work_list(self, number):
        self.wait_text_in_element(OrderLocators.LIST_ORDER_IN_WORK, str(number))

    def wait_header_list_order(self):
        self.wait_for_element_visible(BaseLocators.HEADER_ORDER_LIST)