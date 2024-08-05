from locators.login_locators import *
from locators.main_locators import *
from pages.base_page import *
from data import *


class LoginPage(BasePage):
    @allure.step('Заполняем поле email')
    def set_email(self):
        self.add_text_to_element(TestLoginPage.SEARCH_INPUT_EMAIL, TEST_EMAIL)

    @allure.step('Заполняем поле пароль')
    def set_password(self):
        self.add_text_to_element(TestLoginPage.SEARCH_INPUT_PASSWORD, TEST_PASSWORD)

    @allure.step('Нажимаем кнопку войти и возвращаем текст со страницы создания заказа')
    def check_button_login(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestLoginPage.CLICK_BUTTON_LOGIN)
        self.find_element_with_wait(TestMainLocators.SEARCH_TEXT_BURGER)
