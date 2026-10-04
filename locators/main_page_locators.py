from selenium.webdriver.common.by import By


class Locators:
    
    HEADER_COLLECT_BURGER = (By.XPATH, "//*[text() = 'Соберите бургер']")
    INGRIDIENT = (By.XPATH, "(//*[text() = 'Соус Spicy-X'])[1]")
    HEADER_INGREDIENT_DETALS = (By.XPATH, "//*[text() = 'Детали ингредиента']")
    BUTTON_CLOSE_DETALS = (By.XPATH, "//*[text() = 'Детали ингредиента']/parent::div/following-sibling::button")
    INGRIDIENT = (By.XPATH, "(//*[text() = 'Соус Spicy-X'])[1]")
    COUNTER_INGRIDIENT = (By.XPATH, "(//*[text() = 'Соус Spicy-X'])[1]/parent::a//div[contains(@class, 'counter_counter')]/p")


    