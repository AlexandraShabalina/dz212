from FW.application_manager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_method(self):
        pass
        #self.APP.main_page_ya.open_main_page('https://ya.ru/')


    def teardown_method(self):
        self.APP.main_page_yandex.allure_screenshot()

    def setup_class(self):
        self.APP.main_page_yandex.open_main_page('http://yandex.ru/')

    def teardown_class(self):
        self.APP.stop_driver()
