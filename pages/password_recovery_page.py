from locators.password_recovery_locators import *
from locators.login_locators import *
from pages.base_page import *
from data import *


class PasswordRecoveryPage(BasePage):
    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def check_button_password_recovery(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestPasswordRecoveryLocators.CLICK_BUTTON_PASSWORD_RECOVERY)

    @allure.step('Возвращаем текст с кнопки "Восстановить"')
    def check_button_recovery(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        return self.get_text_from_element(TestPasswordRecoveryLocators.CLICK_BUTTON_RECOVERY)

    @allure.step('Заполняем поле email')
    def set_email(self):
        self.add_text_to_element(TestPasswordRecoveryLocators.SEARCH_INPUT_EMAIL, TEST_EMAIL)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def check_click_button_recovery(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestPasswordRecoveryLocators.CLICK_BUTTON_RECOVERY)

    @allure.step('Возвращаем текст "Восстановление пароля"')
    def check_text_recovery(self):
        return self.get_text_from_element(TestPasswordRecoveryLocators.SEARCH_TEXT_RECOVERY)

    @allure.step('Нажимаем на кнопку скрыть/открыть пароль')
    def check_click_button_show_hide(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestPasswordRecoveryLocators.CLICK_BUTTON_SHOW_HIDE)

    @allure.step('Проверяем, что элемент стал активным')
    def check_button_show_hide_visibility(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        return self.find_element_with_wait(TestPasswordRecoveryLocators.SEARCH_STATUS_ACTIVE)
