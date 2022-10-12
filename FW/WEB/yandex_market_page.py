import allure
from selenium.webdriver.common.by import By

from FW.WEB.search_page import SearchPage


class Locator:
    min_price = (By.XPATH, '//div[@data-filter-id="glprice"]//*[@data-auto="filter-range-min"]//input')
    price_popular_offers = (By.XPATH, '//*[@class="L0ej-"]')
    price_all = (By.XPATH, '//article//*[@class="cia-cs"]//*[@data-autotest-currency="₽"]')
    lenovo = (By.XPATH, '//*[@data-filter-id="7893318"]//label[@data-auto="filter-list-item-152981"]//span[''@class="_2XaWK"]')
    lenovo_popular_offers = (By.XPATH, '//*[@data-zone-name="offer"]//div[@class="cia-cs"]')
    lenovo_all = (By.XPATH, '//article//h3')




class YandexMarketPage(SearchPage):

    @allure.step('Ввод минимальной цены')
    def input_min(self, text):
        self.send_keys(Locator.min_price, text)

    @allure.step('Получение списка цен')
    def get_list_price(self):
        web_element = self.find_elements(Locator.price_popular_offers)
        web_element += self.find_elements(Locator.price_all)
        return web_element

    @allure.step('Нажатие на галочку производителя lenovo')
    def clik_lenovo(self):
        self.click(Locator.lenovo)


    @allure.step('Получение списка цен')
    def get_list_lenovo(self):
        web_element = self.find_elements(Locator.lenovo_popular_offers)
        web_element += self.find_elements(Locator.lenovo_all)
        return web_element


