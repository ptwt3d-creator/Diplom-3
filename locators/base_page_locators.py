from selenium.webdriver.common.by import By


class Locators:
    
    CONSTRUCTOR = (By.XPATH, "//*[text() = 'Конструктор']")
    LIST_ORDER_BUTTON = (By.XPATH, "//*[text() = 'Лента Заказов']")
    MODAL_OVERLAY = (By.XPATH, "(//*[contains(@class, 'Modal_modal_overlay')])[1]")