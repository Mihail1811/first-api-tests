from request import Request


class TestCase:
    def __init__(self):
        self.request = Request()
        self.ID = str()
        self.response = str()

    def create_animal(self, name: str = 'Olaf') -> str:
        """
        Создание нового животного через API-запрос
        :param name: Имя животного, по умолчанию - Olaf
        :return: id созданного животного
        """
        data = {
                       "id": 0,
                       "category": {
                           "id": 0,
                           "name": "string"
                       },
                       "name": name,
                       "photoUrls": [
                           "string"
                       ],
                       "tags": [
                           {
                               "id": 0,
                               "name": "string"
                           }
                       ],
                       "status": "available"
                    }
        self.response = self.request.send_request('post', 'pet', data)
        self.ID = self.response.json()['id']
        return self.ID

    def find_animal(self, animal_id: str) -> dict:
        """
        Метод ищет животное по id
        :param animal_id: id животного
        :return: информация о животном
        """
        url = 'pet/' + str(animal_id)
        self.response = self.request.send_request('get', url)
        return self.response.json()

    def delete_animal(self, animal_id: str) -> dict:
        """
            Удаление животного по его ID через API-запрос.
            :param animal_id: ID животного
            :return: Данные, содержащие информацию об успехе или ошибке.
        """
        url = 'pet/' + str(animal_id)
        self.response = self.request.send_request('delete', url)
        return self.response.json()

    def create_pet(self, name: str = 'Друг') -> str:
        """
            Создание нового животного через API-запрос
            :param name: Имя животного, по умолчанию - Olaf
            :return: id созданного животного
        """
        data = {
                       "id": 337,
                       "category": {
                           "id": 1,
                           "name": "string"
                       },
                       "name": name,
                       "photoUrls": [
                           "string"
                       ],
                       "tags": [
                           {
                               "id": 0,
                               "name": "string"
                           }
                       ],
                       "status": "available"
                    }
        self.response = self.request.send_request('post', 'pet', data)
        self.ID = self.response.json()['id']
        return self.ID

    def check_pet(self, pet_id: str) -> dict:
        """
            Метод ищет животное по id
            :param pet_id: id животного
            :return: информация о животном
        """
        url = 'pet/' + str(pet_id)
        self.response = self.request.send_request('get', url)
        return self.response.json()

    def delete_pet(self, pet_id: str) -> dict:
        """
            Удаление животного по его ID через API-запрос.
            :param pet_id: ID животного
            :return: Данные, содержащие информацию об успехе или ошибке.
        """
        url = 'pet/' + str(pet_id)
        self.response = self.request.send_request('delete', url)
        return self.response.json()

    def find_pets_by_status(self, status: str) -> dict:
        """
            Получение списка животных по указанному статусу через API-запрос.
            :param status: Статус животного
            :return: Список данных о всех животных с указанным статусом.
        """
        url = f'pet/findByStatus?status={status}'
        self.response = self.request.send_request('get', url)
        return self.response.json()
