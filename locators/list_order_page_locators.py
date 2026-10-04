from selenium.webdriver.common.by import By


class Locators:
    HEADER_ORDER_LIST = (By.XPATH, "//*[text() = 'Лента заказов']")
    COUNTER_ORDERS_COMLITE_ALL_TIME = (By.XPATH, "//*[text() = 'Выполнено за все время:']/following-sibling::p")
    COUNTER_ORDERS_COMLITE_TO_DAY = (By.XPATH, "//*[text() = 'Выполнено за сегодня:']/following-sibling::p")
    LIST_ORDER_IN_WORK = (By.XPATH, "//*[text() = 'В работе:']/parent::div//following-sibling::ul[contains(@class, 'OrderFeed_orderListReady')]")