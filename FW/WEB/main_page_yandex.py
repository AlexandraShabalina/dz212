import allure
from selenium.webdriver.common.by import By

from FW.WEB.any_page import AnyPage


class Locator:
    min_price = (By.XPATH, '//div[@data-filter-id="glprice"]//*[@data-auto="filter-range-min"]//input')
    search_input = (By.XPATH, '//*[@name="text"]')
    locator_frame = (By.XPATH, '//form[@action="https://yandex.ru/search/"]/iframe')
    btn_submit = (By.XPATH, '//*[@type="submit"]')
    text_weather = (By.XPATH, '//div[@class="informers3"]/a[1]')
    video = (By.XPATH, '''//a[@class="dzen-top-controls-desktop__button-R4"]//*[contains(text(), 'Видео')]''')




class MainPageYandex(AnyPage):

    @allure.step('Ввод текста в строку поиска')
    def send_keys_in_search_input(self, text):
        frame = self.find_element(Locator.locator_frame)
        self.get_driver().switch_to.frame(frame)
        self.send_keys(Locator.search_input, text)
        self.get_driver().switch_to.default_content()
        return self

    @allure.step('Нажать кнопку Найти')
    def click_btn_submit(self):
        frame = self.find_element(Locator.locator_frame)
        self.get_driver().switch_to.frame(frame)
        self.click(Locator.btn_submit)
        self.get_driver().switch_to.default_content()


    @allure.step('сохранение дескриптора окна')
    def before_current_window_handle(self):
        window_before = self.get_driver().window_handles[0]

    @allure.step('переход на другое окно')
    def after_current_window_handle(self):
        window_after = self.get_driver().window_handles[1]
        self.get_driver().switch_to.window(window_after)

    @allure.step('Нажатие на ссылку видео')
    def clik_video(self):
        self.click(Locator.video)

