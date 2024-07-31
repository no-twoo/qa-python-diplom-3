from selenium.webdriver.common.by import By


class TestPersonalAccountLocators:
    CLICK_BUTTON_PERSONAL_ACCOUNT = [By.XPATH, ".//p[text()='Личный Кабинет']"]
    SEARCH_TEXT_PROFILE = [By.XPATH, ".//a[text()='Профиль']"]
    CLICK_BUTTON_ORDERS_HISTORY = [By.XPATH, ".//a[text()='История заказов']"]
    SEARCH_TEXT_ORDER = [By.XPATH, ".//h2[text()='Флюоресцентный бургер']"]
    CLICK_BUTTON_EXIT = [By.XPATH, ".//button[text()='Выход']"]
