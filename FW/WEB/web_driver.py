import allure
from selenium import webdriver


class WebDriver:

    @allure.step('Запуск и открытие на полный экран браузера')
    def driver_start(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver

    @allure.step('Выход из браузера')
    def driver_exit(self, driver):
        driver.quit()