import allure
import pytest
from selenium.webdriver import Keys
import time
from tests.test_base import TestBase


@allure.epic('Web')
@allure.feature('MainPage')
@allure.story('Yandex')
class TestMainPageYandex(TestBase):

    @allure.title('Проверка кнопки Найти (Test #1)')
    @pytest.mark.WebTest
    @pytest.mark.YaRu
    def test_4(self):
        self.APP.main_page_yandex.before_current_window_handle()
        self.APP.main_page_yandex.clik_video()
        self.APP.main_page_yandex.after_current_window_handle()


        self.APP.video_page.send_keys_in_search_input('Кавказская пленница')
        self.APP.video_page.click_enter()



        print(self.APP.video_page.test_get_web_elements_in_search())

