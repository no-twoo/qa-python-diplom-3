from conftest import *
import pytest
from pages.password_recovery_page import *
from data import *
import allure


class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('Тест проверяет, что работает переход на страницу восстановления пароля по '
                        'кнопке "Восстановить пароль"')
    def test_button_password_recovery(self, driver):
        password_recovery = PasswordRecoveryPage(driver, LOGIN_URL)
        password_recovery.check_button_password_recovery()
        actual_result = password_recovery.check_button_recovery()

        assert actual_result == TEXT_7

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    @allure.description('Тест проверяет, что можно ввести почту и нажать кнопку "Восстановить"')
    def test_email_and_button_recovery(self, driver):
        button_recovery = PasswordRecoveryPage(driver, PASSWORD_RECOVERY_URL)
        button_recovery.set_email()
        button_recovery.check_click_button_recovery()
        actual_result = button_recovery.check_text_recovery()

        assert actual_result == TEXT_8

    @allure.title('Проверка активности поля "Пароль" после нажатия кнопки показать/скрыть')
    @allure.description('Тест проверяет, что клик по кнопке показать/скрыть пароль делает поле '
                        'активным — подсвечивает его')
    def test_click_button_show_hide(self, driver):
        button_show_hide = PasswordRecoveryPage(driver, PASSWORD_RECOVERY_URL)
        button_show_hide.set_email()
        button_show_hide.check_click_button_recovery()
        button_show_hide.check_click_button_show_hide()

        assert button_show_hide.check_button_show_hide_visibility() is not None
