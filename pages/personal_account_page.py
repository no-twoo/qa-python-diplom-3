from locators.personal_account_locators import *
from locators.login_locators import *
from pages.base_page import *


class PersonalAccountPage(BasePage):
    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestPersonalAccountLocators.CLICK_BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Переходим в личный кабинет и возвращаем текст со станицы')
    def check_transition_button_personal_account(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestPersonalAccountLocators.CLICK_BUTTON_PERSONAL_ACCOUNT)
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        return self.get_text_from_element(TestPersonalAccountLocators.SEARCH_TEXT_PROFILE)

    @allure.step('Переходим в историю заказов и возвращаем название заказа')
    def check_transition_button_history_orders(self):
        self.click_to_element(TestPersonalAccountLocators.CLICK_BUTTON_ORDERS_HISTORY)
        return self.get_text_from_element(TestPersonalAccountLocators.SEARCH_TEXT_ORDER)

    @allure.step('Нажимаем кнопку "Выйти"')
    def check_button_logout(self):
        self.click_to_element(TestPersonalAccountLocators.CLICK_BUTTON_EXIT)
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        return self.get_text_from_element(TestLoginPage.CLICK_BUTTON_LOGIN)
