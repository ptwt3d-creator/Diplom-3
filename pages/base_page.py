from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators.base_page_locators import Locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_element_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def wait_for_element_invisibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def drag_and_drop_element(self, locator1, locator2):

        form = self.driver.find_element(*locator1)
        target = self.driver.find_element(*locator2)
        
        # Магия js, перетаскивает элемент а на элемент б
        js_script = """
        var dt = new DataTransfer();
        arguments[0].dispatchEvent(new DragEvent('dragstart', {dataTransfer: dt, bubbles: true}));
        arguments[1].dispatchEvent(new DragEvent('drop', {dataTransfer: dt, bubbles: true}));
        arguments[0].dispatchEvent(new DragEvent('dragend', {dataTransfer: dt, bubbles: true}));
        """
        # Вызов скрипта, передача данных
        self.driver.execute_script(js_script, form, target)

    def wait_text_in_element(self, locator, expected_text, time=10):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, expected_text))

    def wait_text_not_in_element(self, locator, expected_text, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.text_to_be_present_in_element(locator, expected_text))
    
    def wait_text_not_in_element_list_variants(self, locator, expected_variants, time=10):
        return WebDriverWait(self.driver, time).until(lambda _: self.find_element(locator).text not in expected_variants) # Лямбда смотрит в условие - когда условие не выполнилось, через короткое время (~0.5 секуды) WebDriverWait снова вызывает лямбду которая снова проверяет условие

    def get_text_from_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return element.text
    
    def js_wait_click(self, locator, time=10):
        # Ждем только того, что элемент технически загрузился в DOM-дерево страницы (presence)
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        # js-клик
        self.driver.execute_script("arguments[0].click();", element)

class CommonPage(BasePage):

    def wait_click_list_orders_button(self):
        element = self.wait_for_element_clickable(Locators.LIST_ORDER_BUTTON)
        element.click()
    
    def wait_click_constructor_button(self):
        element = self.wait_for_element_clickable(Locators.CONSTRUCTOR)
        element.click()
    
    def wait_header_list_order(self):
        self.wait_for_element_visible(Locators.LIST_ORDER_BUTTON)
    
    def wait_invisibility_modal_overlay(self):
        self.wait_for_element_invisibility(Locators.MODAL_OVERLAY)

    # Из-за оверлея работает тольо js
    def js_wait_click_list_order_button(self):
        self.js_wait_click(Locators.LIST_ORDER_BUTTON)