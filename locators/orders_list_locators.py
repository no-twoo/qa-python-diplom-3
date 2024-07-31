from selenium.webdriver.common.by import By


class TestOrdersListLocators:
    CLICK_BUTTON_ORDER = [By.XPATH, ".//li[1][contains(@class, 'OrderHistory_listItem')]"]
    SEARCH_COMPOUND = [By.XPATH, ".//p[text()='Cостав']"]
    SEARCH_COMPLETE_ALL_TIME = [By.XPATH, ".//p[text()='Выполнено за все время:']//"
                                          "following::p[1][contains(@class, 'OrderFeed_number')]"]
    SEARCH_COMPLETE_TODAY = [By.XPATH, ".//p[text()='Выполнено за сегодня:']//"
                                       "following::p[contains(@class, 'OrderFeed_number')]"]
    SEARCH_IN_WORK = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]//li[1]"]
    SEARCH_NAME_ORDER = [By.XPATH, ".//h2[text()='Флюоресцентный бургер']"]
