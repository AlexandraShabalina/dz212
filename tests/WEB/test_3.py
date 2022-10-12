import allure
import pytest
from selenium.webdriver import Keys
import time
from tests.test_base import TestBase


@allure.epic('Web')
@allure.feature('MainPage')
@allure.story('Yandex')
class TestMainPageYandex(TestBase):

    @allure.title('Задание 3')
    @pytest.mark.WebTest
    @pytest.mark.YaRu
    def test_3(self):
        main_page = self.APP.main_page_yandex
        main_page.send_keys_in_search_input('Погода')
        main_page.before_current_window_handle()
        main_page.click_btn_submit()
        main_page.after_current_window_handle()

        self.APP.search_page.click_link2()
        self.APP.search_page.after_current_window_handle2()

        self.APP.pogoda_page.send_keys_in_search_input('Москва')
        self.APP.pogoda_page.click_enter()
        time.sleep(5)


        city = self.APP.pogoda_page.get_city_name()
        try:
            assert 'Москва' in city
        except:
            self.APP.yandex_market_page.allure_screenshot()
            raise