from pages.base_page import CommonPage
from locators.login_page_locators import Locators

class LoginPage(CommonPage):
    
    def wait_click_login_button(self):
        element = self.wait_for_element_clickable(Locators.LOGIN_BUTTON)
        element.click()

    def login_on_site(self):
        self.wait_for_element_clickable(Locators.EMAIL_FIELD).send_keys("AlexanderSobolev51_999@yandex.ru")
        self.wait_for_element_clickable(Locators.PASSWORD_FIELD).send_keys("42314231")
        self.wait_click_login_button()

