import pytest
from selenium import webdriver
from pages.main_page import MainPage


class TestMainFunc:

    def test_open_details(self, main_page_function_scope):
        main_page_function_scope.wait_click_ingredient()
        main_page_function_scope.wait_window_details()
    
    def test_close_detals(self, main_page_function_scope):
        main_page_function_scope.wait_click_ingredient()
        main_page_function_scope.wait_window_details()
        main_page_function_scope.wait_click_close_details_button()
        main_page_function_scope.wait_close_details()
    

    