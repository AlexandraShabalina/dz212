import allure

from FW.API.api_base_fw import ApiBaseFw


@allure.epic('Api')
@allure.feature('Task')
@allure.story('Create Task')
class CreateTask(ApiBaseFw):

    @allure.step('Создание задачи. post /api/Tasks')
    def post_tasks(self, body, params=None):
        return self.request_post(f'{self.manager.settings.url_api} + /api/Tasks', body, params)

    def create_tasks_body(self):
        url = f'{self.manager.settings.url_api}/api/Tasks'

        body = {
            'subject': 'task1',
            'descriptionContent': [
                {
                    'type': 'Text',
                    'text': 'task1'
                },
            ],
            'contractorId': self.manager.settings.users['test_user01']['user_id'],
        }
        responce = self.request_post(url=url, body=body)
        return responce

    @allure.title('Отклонить задачу')
    def reject_task(self, synctoken, task_id, text='AutomationApiTest Reject'):
        # Формируем тело запроса для отклонения
        task_body = {
            'text': text,
            'syncToken': synctoken,
        }

        # Отклоняем задачу
        task = self.put_tasks_id_actions_reject(task_id, task_body)