import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from FW.WEB.search_page import SearchPage


class Locator:
    search_input = (By.XPATH,'//*[@class="mini-suggest-form__input mini-suggest__input"]')
    city = (By.XPATH, '//*[@id="main_title"]')


class PogodaPage(SearchPage):


    @allure.step('Ввод текста в строку поиска')
    def send_keys_in_search_input(self, text):
        self.send_keys(Locator.search_input, text)
        return self

    @allure.step('Нажать ENTER')
    def click_enter(self):
        self.send_keys_in_search_input(Keys.ENTER)

    @allure.step('Получение названия города')
    def get_city_name(self):
        return self.get_text(Locator.city)