from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:

    @allure.step('Открываем браузер Firefox и передаем url')
    def __init__(self, driver, url, time=10):
        self.driver = driver
        self.driver.get(url)
        self.time = time

    @allure.step('Ожидаем и находим элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, self.time).until(expected_conditions.visibility_of_element_located(
            locator))

        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавляем текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Возвращаем текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Ожидаем, пока элемент станет невидимым')
    def invisibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(
            locator))

    @allure.step('Перемещаем элемент с одним локатором в другой локатор')
    def drag_and_drop_on_element(self, source_locator, new_locator):
        source = self.driver.find_element(*source_locator)
        destination = self.driver.find_element(*new_locator)
        ActionChains(self.driver).click_and_hold(source).move_to_element(destination).release().perform()
