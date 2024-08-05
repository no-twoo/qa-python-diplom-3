from selenium.webdriver.common.by import By


class TestPasswordRecoveryLocators:
    CLICK_BUTTON_PASSWORD_RECOVERY = [By.XPATH, ".//a[text()='Восстановить пароль']"]
    SEARCH_INPUT_EMAIL = [By.XPATH, ".//input[@type='text']"]
    CLICK_BUTTON_RECOVERY = [By.XPATH, ".//button[text()='Восстановить']"]
    CLICK_BUTTON_SHOW_HIDE = [By.XPATH, ".//div[contains(@class, 'input__icon')]"]
    SEARCH_TEXT_RECOVERY = [By.XPATH, ".//h2[text()='Восстановление пароля']"]
    SEARCH_STATUS_ACTIVE = [By.XPATH, ".//div[contains(@class, 'input_status_active')]"]
