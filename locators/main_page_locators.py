from selenium.webdriver.common.by import By


class Locators:
    
    HEADER_COLLECT_BURGER = (By.XPATH, "//*[text() = 'Соберите бургер']")
    INGRIDIENT = (By.XPATH, "(//*[text() = 'Соус Spicy-X'])[1]")
    HEADER_INGREDIENT_DETALS = (By.XPATH, "//*[text() = 'Детали ингредиента']")
    BUTTON_CLOSE_DETAILS = (By.XPATH, "//*[text() = 'Детали ингредиента']/parent::div/following-sibling::button")
    INGRIDIENT = (By.XPATH, "(//*[text() = 'Соус Spicy-X'])[1]")
    COUNTER_INGRIDIENT = (By.XPATH, "(//*[text() = 'Соус Spicy-X'])[1]/parent::a//div[contains(@class, 'counter_counter')]/p")
    BASKET_INGREDIENTS = (By.XPATH, "(//*[contains(@class, 'BurgerConstructor_basket')])[1]")
    BUN = (By.XPATH, "(//*[text() = 'Флюоресцентная булка R2-D3'])[1]")
    ORDER_CREATE_BUTTON = (By.XPATH, "//*[text() = 'Оформить заказ']")
    BUTTON_CLOSE_WINDOW_ORDER_CREATED = (By.XPATH, "//*[text()='идентификатор заказа']/parent::div/following-sibling::button")

    NUMBER_ORDER_IN_ORDER_CREATED = (By.XPATH, "//*[contains(@class, 'Modal_modal__title_shadow')]")

    CREATED_ORDER_WINDOW = (By.XPATH, "//*[text()='идентификатор заказа']")