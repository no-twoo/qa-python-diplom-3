from conftest import *
import pytest
from pages.orders_list_page import *
from pages.main_page import *
from pages.login_page import *
from pages.personal_account_page import *
from data import *
import allure


class TestOrdersList:
    @allure.title('Проверка открытия всплывающего окна с деталями')
    @allure.description('Тест проверяет, если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_pop_up_window_with_details(self, driver):
        pop_up_window = OrdersList(driver, ORDERS_LIST_URL)

        assert pop_up_window.pop_up_window_with_details() == TEXT_6

    @allure.title('Проверка увеличения счетчика выполненных заказов за все время')
    @allure.description('Тест проверяет, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @pytest.mark.usefixtures("login")
    def test_counter_increases_complete_all_time(self, driver):
        if driver.name == "firefox":
            return

        complete_all_time = OrdersList(driver, ORDERS_LIST_URL)
        expected_result = complete_all_time.counter_increases_complete_all_time()
        create_order = MainPage(driver, MAIN_URL)
        create_order.drag_and_drop()
        create_order.check_click_button_create_order()
        create_order.click_button_close_order()
        create_order.click_transition_button_orders_list()
        actual_result = complete_all_time.counter_increases_complete_all_time()

        assert expected_result < actual_result

    @allure.title('Проверка увеличения счетчика выполненных заказов за день')
    @allure.description('Тест проверяет, что при создании нового заказа счётчик Выполнено за день увеличивается')
    @pytest.mark.usefixtures("login")
    def test_counter_increases_complete_today(self, driver):
        if driver.name == "firefox":
            return

        complete_all_time = OrdersList(driver, ORDERS_LIST_URL)
        expected_result = complete_all_time.counter_increases_complete_today()
        create_order = MainPage(driver, MAIN_URL)
        create_order.drag_and_drop()
        create_order.check_click_button_create_order()
        create_order.click_button_close_order()
        create_order.click_transition_button_orders_list()
        actual_result = complete_all_time.counter_increases_complete_today()

        assert expected_result < actual_result

    @allure.title('Проверка появления номера созданного заказа в разделе "В работе"')
    @allure.description('Тест проверяет, что после оформления заказа его номер появляется в разделе В работе')
    @pytest.mark.usefixtures("login")
    def test_order_number_appeared_in_work(self, driver):
        if driver.name == "firefox":
            return

        create_order = MainPage(driver, MAIN_URL)
        create_order.drag_and_drop()
        create_order.check_click_button_create_order()
        expected_result = create_order.check_number_order()
        create_order.click_button_close_order()
        create_order.click_transition_button_orders_list()
        order_number_appeared = OrdersList(driver, ORDERS_LIST_URL)
        actual_result = order_number_appeared.appears_number_in_work()

        assert expected_result == actual_result

    @allure.title('Проверка отображения заказов из "Истории заказов" на странице "Лента заказов"')
    @allure.description('Тест проверяет, что заказы пользователя из раздела "История заказов" отображаются на '
                        'странице "Лента заказов"')
    @pytest.mark.usefixtures("login")
    def test_displaying_orders_from_order_history(self, driver):
        if driver.name == "firefox":
            return

        create_order = MainPage(driver, MAIN_URL)
        create_order.drag_and_drop()
        create_order.check_click_button_create_order()
        create_order.click_button_close_order()
        personal_account = PersonalAccountPage(driver, MAIN_URL)
        personal_account.click_button_personal_account()
        expected_result = personal_account.check_transition_button_history_orders()
        transition_orders_list = MainPage(driver, MAIN_URL)
        transition_orders_list.check_transition_button_orders_list()
        displaying_orders = OrdersList(driver, ORDERS_LIST_URL)
        actual_result = displaying_orders.displaying_orders_from_order_list()

        assert expected_result == actual_result
