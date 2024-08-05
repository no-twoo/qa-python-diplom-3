from locators.main_locators import *
from locators.login_locators import *
from pages.base_page import *


class MainPage(BasePage):
    @allure.step('Переходим по клику на "Конструктор" и возвращаем текст со страницы создания заказа')
    def check_transition_button_constructor(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestMainLocators.CLICK_BUTTON_ORDERS_LIST)
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestMainLocators.CLICK_BUTTON_CONSTRUCTOR)
        return self.get_text_from_element(TestMainLocators.SEARCH_TEXT_BURGER)

    @allure.step('Переходим по клику на "Лента Заказов"')
    def click_transition_button_orders_list(self):
        self.click_to_element(TestMainLocators.CLICK_BUTTON_ORDERS_LIST)

    @allure.step('Переходим по клику на "Лента Заказов" и возвращаем со станицы ленты заказов')
    def check_transition_button_orders_list(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestMainLocators.CLICK_BUTTON_ORDERS_LIST)
        return self.get_text_from_element(TestMainLocators.SEARCH_TEXT_ORDERS_LIST)

    @allure.step('Переходим по клику на ингредиент и возвращаем детали ингредиента')
    def check_click_to_ingredient(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestMainLocators.SEARCH_INGREDIENT)
        return self.get_text_from_element(TestMainLocators.SEARCH_INGREDIENT_DETAILS)

    @allure.step('Закрываем детали ингредиента и возвращаем текст со страницы создания заказов')
    def check_click_to_icon_exit(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestMainLocators.SEARCH_INGREDIENT)
        self.click_to_element(TestMainLocators.SEARCH_ICON_EXIT)
        return self.get_text_from_element(TestMainLocators.SEARCH_TEXT_BURGER)

    @allure.step('Переносим ингредиент в поле создания бургера')
    def drag_and_drop(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.drag_and_drop_on_element(TestMainLocators.SEARCH_INGREDIENT, TestMainLocators.CHECK_CREATE_BURGER)

    @allure.step('Проверяем, что после добавления ингредиента, изменился его каунтер')
    def check_increases_counter_ingredient(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.find_element_with_wait(TestMainLocators.SEARCH_INGREDIENT)
        self.drag_and_drop_on_element(TestMainLocators.SEARCH_INGREDIENT, TestMainLocators.CHECK_CREATE_BURGER)
        return self.get_text_from_element(TestMainLocators.SEARCH_COUNTER)

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def check_click_button_create_order(self):
        self.click_to_element(TestMainLocators.CLICK_BUTTON_CREATE_ORDER)
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)

    @allure.step('Закрываем детали оформленного заказа')
    def click_button_close_order(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.click_to_element(TestMainLocators.CLICK_BUTTON_CLOSE_ORDER)

    @allure.step('Возвращаем номер оформленного заказа')
    def check_number_order(self):
        return self.get_text_from_element(TestMainLocators.SEARCH_NUMBER_ORDER)

    @allure.step('Оформляем заказ и возвращаем текст, что заказ начали готовить')
    def check_create_order_login_user(self):
        self.invisibility_of_element(TestLoginPage.SEARCH_ELEMENT)
        self.drag_and_drop_on_element(TestMainLocators.SEARCH_INGREDIENT, TestMainLocators.CHECK_CREATE_BURGER)
        self.click_to_element(TestMainLocators.CLICK_BUTTON_CREATE_ORDER)
        return self.get_text_from_element(TestMainLocators.SEARCH_TEXT_SUCCESSFUL)
