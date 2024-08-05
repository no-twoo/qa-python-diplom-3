from locators.orders_list_locators import *
from locators.login_locators import *
from pages.base_page import *


class OrdersList(BasePage):
    @allure.step('Нажимаем на заказ и возвращаем текст с деталями заказа')
    def pop_up_window_with_details(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestOrdersListLocators.CLICK_BUTTON_ORDER)
        return self.get_text_from_element(TestOrdersListLocators.SEARCH_COMPOUND)

    @allure.step('Возвращаем кол-во заказов за все время')
    def counter_increases_complete_all_time(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        return self.get_text_from_element(TestOrdersListLocators.SEARCH_COMPLETE_ALL_TIME)

    @allure.step('Возвращаем кол-во заказов за сегодня')
    def counter_increases_complete_today(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        return self.get_text_from_element(TestOrdersListLocators.SEARCH_COMPLETE_TODAY)

    @allure.step('Возвращаем номер заказа в работе')
    def appears_number_in_work(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        return self.get_text_from_element(TestOrdersListLocators.SEARCH_IN_WORK)

    @allure.step('Возвращаем название заказа из Ленты Заказов')
    def displaying_orders_from_order_list(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        return self.get_text_from_element(TestOrdersListLocators.SEARCH_NAME_ORDER)
