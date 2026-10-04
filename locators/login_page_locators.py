from selenium.webdriver.common.by import By


class Locators:
    
    EMAIL_FIELD = (By.XPATH, "//*[text() = 'Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//*[text() = 'Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//*[text() = 'Войти']")