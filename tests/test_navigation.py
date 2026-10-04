import pytest
from selenium import webdriver
from pages.base_page import CommonPage

class TestNavigation:

    def test_list_order_button_navigation(self, main_page_function_scope):
        main_page_function_scope.wait_click_list_orders_button()
        main_page_function_scope.wait_header_list_order()
    
    def test_constructor_button_navigation(self, main_page_function_scope):
        main_page_function_scope.wait_click_list_orders_button()
        main_page_function_scope.wait_header_list_order()

