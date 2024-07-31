from selenium.webdriver.common.by import By


class TestMainLocators:
    CLICK_BUTTON_CONSTRUCTOR = [By.XPATH, ".//p[contains(text(), 'Конструктор')]"]
    CLICK_BUTTON_ORDERS_LIST = [By.XPATH, ".//p[contains(text(), 'Лента Заказов')]"]
    SEARCH_TEXT_BURGER = [By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]"]
    SEARCH_TEXT_ORDERS_LIST = [By.XPATH, ".//h1[contains(text(), 'Лента заказов')]"]
    SEARCH_INGREDIENT = [By.XPATH, ".//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]"]
    SEARCH_INGREDIENT_DETAILS = [By.XPATH, ".//h2[text()='Детали ингредиента']"]
    SEARCH_ICON_EXIT = [By.XPATH, ".//button[@type='button']"]
    CHECK_CREATE_BURGER = [By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]"]
    SEARCH_COUNTER = [By.XPATH, ".//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]"
                                "//ancestor::p[contains(@class, 'counter_counter')]"]
    CLICK_BUTTON_CREATE_ORDER = [By.XPATH, ".//button[text()='Оформить заказ']"]
    SEARCH_TEXT_SUCCESSFUL = [By.XPATH, ".//p[text()='Ваш заказ начали готовить']"]
    CLICK_BUTTON_CLOSE_ORDER = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified')]"]
    SEARCH_NUMBER_ORDER = [By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]"]
