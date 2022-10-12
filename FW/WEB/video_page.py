import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from FW.WEB.main_page_yandex import MainPageYandex



class Locator:
    search_input = (By.XPATH, '//input[@class="zen-ui-search__input"]')
    title_ = (By.XPATH, f'''//*[@class="feed__row"]//a[contains(text(), 'Кавказская пленница')]''')

class VideoPage(MainPageYandex):

        @allure.step('Ввод в строку поиска видео')
        def send_keys_in_search_input(self, text):
            self.send_keys(Locator.search_input, text)

        @allure.step('Нажать ENTER')
        def click_enter(self):
            self.send_keys_in_search_input(Keys.ENTER)

        @allure.step('Выбор элементов после поиска видео')
        def test_get_web_elements_in_search(self):
            return len(self.find_elements(Locator.title_))