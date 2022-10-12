import allure

from FW.API.api_base_fw import ApiBaseFw


class Users(ApiBaseFw):

    @allure.step('получение профиля gjkmpjdfntkz по id')
    def get_user_for_id(self, id):
        return self.request_get(f'{self.manager.settings.url_api}/api/Users/{id}')

    @allure.step('получение профиля пользователя')
    def get_user_profile(self):
        return self.request_get(f'{self.manager.settings.url_api}/api/Users/Profile')


    @allure.step('заполнение полей юзера')
    def filling_in_the_fields(self, user_profile):
        self.manager.settings.users['id'] = user_profile['id']
        self.manager.settings.users['login'] = user_profile['login']
        self.manager.settings.users['email'] = user_profile['email']
        self.manager.settings.users['emailConfirmed'] = user_profile['emailConfirmed']
        self.manager.settings.users['name'] = user_profile['name']
        self.manager.settings.users['middleName'] = user_profile['middleName']