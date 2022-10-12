from FW.API.users import Users
from FW.WEB.main_page_yandex import MainPageYandex
from FW.WEB.web_driver import WebDriver
from FW.API.token import Token
from data.settings import Settings
from FW.WEB.yandex_market_page import YandexMarketPage
from FW.WEB.search_page import SearchPage
from FW.WEB.pogoda_page import PogodaPage
from FW.WEB.video_page import VideoPage
from FW.API.create_task import CreateTask

class ApplicationManager:

    driver = None

    def stop_driver(self):
        self.web_driver.driver_exit(self.driver)
        self.driver = None

    def __init__(self):
        self.settings = Settings()
        self.web_driver = WebDriver()
        self.yandex_market_page = YandexMarketPage(self)
        self.main_page_yandex = MainPageYandex(self)

        self.token = Token(self)
        self.users = Users(self)
        self.create_task = CreateTask(self)
        self.search_page = SearchPage(self)
        self.pogoda_page = PogodaPage(self)
        self.video_page = VideoPage(self)
