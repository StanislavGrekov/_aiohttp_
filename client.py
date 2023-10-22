import aiohttp
import asyncio

# Города, по которым можно получить данные о погоде
cities = ['Poletayevo', 'Miass', 'Chelyabinsk']
# Ключ для работы сервиса Openweathermap
key = ' '

async def main():
    async with aiohttp.ClientSession() as client:
        #1.Создание пользователя
        response = await client.post('http://127.0.0.1:8080/user/',
                                     json={'email': 'dimon@yandex.ru',
                                        'password': '12345678',
                                        'first_name': 'Дмитрий',
                                        'last_name': 'Дмитриев'})

        data = await response.json()
        print(data['answer'])

        # 2.Получение данных пользователя
        # response = await client.get('http://127.0.0.1:8080/user/3')
        #
        # data = await response.json()
        # print(data['answer'])

        # 3.Редактирование пользователя
        # response = await client.patch('http://127.0.0.1:8080/user/3',
        #                              json={'email': 'dimon@yandex.ru',
        #                                 'oldpassword': '12345678',
        #                                 'newpassword': 'password',
        #                                 'first_name': 'Дмитрий',
        #                                 'last_name': 'Дмитриев'})
        #
        # data = await response.json()
        # print(data['answer'])

        # 4.Удаление пользователя
        # response = await client.delete('http://127.0.0.1:8080/user/3',
        #                                json={'email': 'dimon@yandex.ru',
        #                                      'password': 'password',})
        #
        # data = await response.json()
        # print(data['answer'])

        # 5.Создание записей в БД, содержащих данные о погоде в указаных городах
        # response = await client.post('http://127.0.0.1:8080/weather/',
        #                              json={'cities': cities,
        #                                    'APPID': key,
        #                                    'email': 'dimon@yandex.ru',
        #                                     'password': '12345678',
        #                                    })
        # data = await response.json()
        # print(data['answer'])

        # 6.Получение даyных о погоде из БД по email
        # response = await client.get('http://127.0.0.1:8080/weather/',
        #                              json={
        #                                    'email': 'dimon@yandex.ru',
        #                                    })
        # data = await response.json()
        # for element in data['answer']:
        #     print(element)

        # 7.Удаление записей о погоде
        # response = await client.delete('http://127.0.0.1:8080/weather/7',
        #                                json={'email': 'dimon@yandex.ru',
        #                                      'password': '12345678',})
        #
        # data = await response.json()
        # print(data['answer'])

asyncio.run(main())
