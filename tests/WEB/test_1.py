import time

import allure
import pytest
from selenium.webdriver import Keys

from tests.test_base import TestBase


@allure.epic('Web')
@allure.feature('MainPage')
@allure.story('Yandex')
class TestMainPageYandex(TestBase):

    @allure.title('Задание 1')
    @pytest.mark.WebTest
    @pytest.mark.YandexRu
    def test_1(self):
        main_page = self.APP.main_page_yandex
        main_page.send_keys_in_search_input('Купить ноутбук')
        main_page.before_current_window_handle()
        main_page.click_btn_submit()
        main_page.after_current_window_handle()

        self.APP.search_page.click_link()
        self.APP.search_page.after_current_window_handle2()

        self.APP.yandex_market_page.input_min(self.APP.settings.minimal_price)
        time.sleep(7)

    def test_proverka(self):
        windows = self.APP.driver.window_handles
        web_elements = self.APP.yandex_market_page.get_list_price()  # получаем список веб эл
        for element in web_elements:
            text_ = element.text
            for lett in [' ', '₽']:
               if lett in text_:  # проверяем есть ли символы пробела или знака рубля в тексте
                        text_ = text_.replace(lett, '')  # если тру убираем их
            try:
                assert int(text_) > int(self.APP.settings.minimal_price)  # сравниваем поставленную цену с полученной
            except:
                self.APP.yandex_market_page.allure_screenshot()
                raise

        # windows = self.APP.driver.window_handles
        # web_elements = self.APP.yandex_market_page.get_list_price()  # получаем список веб эл
        # for element in web_elements:
        #     text_ = element.text
        #     for lett in [' ', '₽']:
        #         if lett in text_:  # проверяем есть ли символы пробела или знака рубля в тексте
        #             text_ = text_.replace(lett, '')  # если тру убираем их
        #     try:
        #         assert int(text_) > int(
        #             self.APP.settings.minimal_price)  # сравниваем поставленную цену с полученной
        #     except:
        #         self.APP.yandex_market_page.allure_screenshot()
        #         raise