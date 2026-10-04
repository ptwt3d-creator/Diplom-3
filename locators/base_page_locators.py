from selenium.webdriver.common.by import By


class Locators:
    
    CONSTRUCTOR = (By.XPATH, "//*[text() = 'Конструктор']")
    ORDER_LIST = (By.XPATH, "//*[text() = 'Лента Заказов']")
    