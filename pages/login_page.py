from pages.base_page import CommonPage
from locators.login_page_locators import LoginLocators

class LoginPage(CommonPage):
    
    def wait_click_login_button(self):
        element = self.wait_for_element_clickable(LoginLocators.LOGIN_BUTTON)
        element.click()
    
    @allure.step("Ввод email")
    def enter_email(self, email):
        self.wait_for_element_clickable(LoginLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.wait_for_element_clickable(LoginLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Авторизация на сайте")
    def login_on_site(self):
        self.enter_email("AlexanderSobolev51_999@yandex.ru")
        self.enter_password("42314231")
        self.wait_click_login_button()

