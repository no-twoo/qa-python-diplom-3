from conftest import *
import pytest
from pages.personal_account_page import *
from pages.login_page import *
from data import *
import allure


@pytest.mark.usefixtures("login")
class TestPersonalAccount:
    @allure.title('Проверка перехода по клику на "Личный кабинет"')
    @allure.description('Тест проверяет, что переход по клику "Личный кабинет" осуществляется успешно')
    def test_transition_personal_account(self, driver):
        transition_personal_account = PersonalAccountPage(driver, LOGIN_URL)
        actual_result = transition_personal_account.check_transition_button_personal_account()

        assert actual_result == TEXT_9

    @allure.title('Проверка перехода по клику на "История заказов"')
    @allure.description('Тест проверяет, что переход по клику "История заказов" осуществляется успешно')
    def test_transition_history_orders(self, driver):
        transition_history_orders = PersonalAccountPage(driver, LOGIN_URL)
        transition_history_orders.check_transition_button_personal_account()
        actual_result = transition_history_orders.check_transition_button_history_orders()

        assert actual_result == TEXT_10

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Тест проверяет, что можно выйти из аккаунта')
    def test_logout(self, driver):
        logout = PersonalAccountPage(driver, LOGIN_URL)
        logout.check_transition_button_personal_account()
        actual_result = logout.check_button_logout()

        assert actual_result == TEXT_11
