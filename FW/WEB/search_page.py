import allure
from selenium.webdriver.common.by import By

from FW.WEB.main_page_yandex import MainPageYandex



class Locator:
    link = (By.XPATH, '''//a//*[contains(text(), 'market.yandex.ru')]''')
    link2 = ( By.XPATH, '''//a//*[contains(text(), 'yandex')]''')

class SearchPage(MainPageYandex):

    @allure.step('Нажатие по ссылке яндекс маркета')
    def click_link(self):
        self.click(Locator.link)

    @allure.step('Нажатие по ссылке яяндекс погода')
    def click_link2(self):
        self.click(Locator.link2)

    @allure.step('Переход на ссылку')
    def after_current_window_handle2(self):
        window_after = self.get_driver().window_handles[2]
        self.get_driver().switch_to.window(window_after)