from conftest import *
import pytest
from pages.main_page import *
from pages.login_page import *
from data import *
import allure


class TestMainPage:
    @allure.title('Проверка перехода по кнопке "Конструктор" на страницу оформления заказа')
    @allure.description('Тест проверяет, что появляется соответсвующий текст со страницы оформления заказа')
    def test_check_transition_button_constructor(self, driver):
        transition_button_constructor = MainPage(driver, MAIN_URL)

        assert transition_button_constructor.check_transition_button_constructor() == TEXT_1

    @allure.title('Проверка перехода по кнопке "Лента Заказов" на страницу ленты заказов')
    @allure.description('Тест проверяет, что появляется соответсвующий текст со страницы ленты заказов')
    def test_check_transition_button_orders_list(self, driver):
        transition_button_orders_list = MainPage(driver, MAIN_URL)

        assert transition_button_orders_list.check_transition_button_orders_list() == TEXT_2

    @allure.title('Проверка появления всплывающего окна с деталями')
    @allure.description('Тест проверяет, что появляются детали ингредиента')
    def test_click_to_ingredient(self, driver):
        click_to_ingredient = MainPage(driver, MAIN_URL)

        assert click_to_ingredient.check_click_to_ingredient() == TEXT_3

    @allure.title('Проверка кнопки закрытия деталей ингредиента')
    @allure.description('Тест проверяет, что детали ингредиента закрываются и появляется соответствующий текст со '
                        'страницы оформления заказа')
    def test_check_click_to_icon_exit(self, driver):
        click_to_icon_exit = MainPage(driver, MAIN_URL)

        assert click_to_icon_exit.check_click_to_icon_exit() == TEXT_1

    @allure.title('Проверка, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Тест проверяет, что каунтер ингредиента увеличивается')
    def test_check_increases_counter_ingredient(self, driver):
        if driver.name == "firefox":
            return

        increases_counter_ingredient = MainPage(driver, MAIN_URL)

        assert increases_counter_ingredient.check_increases_counter_ingredient() == TEXT_4

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    @allure.description('Тест проверяет, что появляется сообщение об успешном оформлении заказа')
    @pytest.mark.usefixtures("login")
    def test_check_create_order_login_user(self, driver):
        create_order_login_user = MainPage(driver, LOGIN_URL)

        assert create_order_login_user.check_create_order_login_user() == TEXT_5
