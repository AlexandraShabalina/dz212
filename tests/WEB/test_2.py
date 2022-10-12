import allure
import pytest
import time
from tests.test_base import TestBase


@allure.epic('Web')
@allure.feature('MainPage')
@allure.story('Yandex')
class TestMainPageYandex(TestBase):

    @allure.title('Задание 2')
    @pytest.mark.WebTest
    @pytest.mark.YandewRu
    def test_2(self):
        main_page = self.APP.main_page_yandex
        main_page.send_keys_in_search_input('Купить ноутбук') # Ввод в поиск купить ноутбук
        main_page.before_current_window_handle()
        main_page.click_btn_submit() # Нажатие кнопки найти
        main_page.after_current_window_handle()

        self.APP.search_page.click_link() # Переход на страницу яндекс маркета
        self.APP.search_page.after_current_window_handle2()

        self.APP.yandex_market_page.clik_lenovo() # Выбор ноутбуков только леново
        time.sleep(7)


        web_elements = self.APP.yandex_market_page.get_list_lenovo() # Проверка что все ноутбуки леново

        for element in web_elements:
            text = element.text
            try:
                assert self.APP.settings.notebook_brand in text
            except:
                self.APP.yandex_market_page.allure_screenshot()
                raise