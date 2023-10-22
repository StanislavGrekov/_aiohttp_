## Aiohttp
### ТЗ
* Сервис должен отправлять запросы к Openweathermap и получать прогноз погоды по указанным в списке городам,
* Запросы должны выполнять асинхронно,
* Результат запросов записывается в БД,
* Продумать простую регистрацию пользователей.

### Этапы работы:
* Пользователь регистрируется,
* При необходимости пользователь изменяет учетные данные, а также удаляет пользователя (п.1-п.4 файла client.py),
* Пользователь, используя ключ от Openweathermap, аснхронно посылает запросы погоды по указанным в списке городам. Информация запсывается в БД (п.5-п.7 файла client.py),
* В случае необходимости пользователь может построчно удалить информацию о погоде.

### Описание
* Файл server.py содержит классы User, Weather и роуты для выполнения запроосов, 
* Файл func.py содержит функции запросов к Openweathermap и записи в базу,
* Файл client.py содержит запросы к сервису,
* Файл models.py - моделька базы данных.

