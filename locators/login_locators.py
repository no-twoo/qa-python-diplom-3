from selenium.webdriver.common.by import By


class TestLoginPage:
    SEARCH_INPUT_EMAIL = [By.XPATH, ".//*[text()='Email']/following-sibling::input"]
    SEARCH_INPUT_PASSWORD = [By.XPATH, ".//*[text()='Пароль']/following-sibling::input"]
    CLICK_BUTTON_LOGIN = [By.XPATH, ".//button[text()='Войти']"]
    SEARCH_ELEMENT = [By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]"
                                "/following::div[@class='Modal_modal_overlay__x2ZCr']"]
