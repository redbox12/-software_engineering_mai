## Лабораьорная работа №3 
**Предмет: Программная инженерия** <br>
**Выполнил: Королев Иван, М80-114СВ**

1. Для сервиса управления данными (созданного в предыдущей лабораторной
работе) о клиентах создайте долговременное хранилище данных в
реляционной СУБД PostgreSQL 14;
2. Должен быть создан скрипт по созданию базы данных и таблиц, а также
наполнению СУБД тестовыми значениями. Он должен запускаться при первом
запуске вашего сервиса;
3. Для сущности, должны быть созданы запросы к БД (CRUD) согласно ранее
разработанной архитектуре
4. Данные о пользователе должны включать логин и пароль. Пароль должен
храниться в закрытом виде (хэширован) – в этом задании опционально
5. Должно применяться индексирования по полям, по которым будет
производиться поиск
6. При необходимости актуализируйте модель архитектуры в Structurizr DSL
7. Ваши сервисы должны запускаться через docker-compose командой dockercompose up (создайте Docker файлы для каждого сервиса)

Рекомендации по C++
- Используйте фреймворк Poco https://docs.pocoproject.org/current/
- Пример по работе с Poco Web Servers и JWT
https://github.com/DVDemon/arch_lecture_examples/tree/main/hl_mai_lab_01

Рекомендации по Python:
- Используйте FastAPI для построения интерфейсов
- Рекомендуется использовать Pedantic для валидации моделей
- Используйте SQL Alchemy для работы с СУБД
- Простой пример применения SQL Alchemy (code first)
https://github.com/DVDemon/architecture_python/blob/main/03_sql/main.py

## Запуск приложения
1. Установите Docker на компьютер
2. После установки, запустите команду:
```
docker-compose up --build
```

##  Обзор приложения
#### 🟢 http://localhost:8001/docs - приложение user_api_service c Postgresql

## Результаты

1. Для сервиса управления данными (созданного в предыдущей лабораторной
работе) о клиентах создайте долговременное хранилище данных в
реляционной СУБД PostgreSQL 14;
<br>
✅ Выполнено <br>

```
    archdb=# \d
                List of relations
    Schema |     Name     |   Type   | Owner
    --------+--------------+----------+-------
    public | users        | table    | root
    public | users_id_seq | sequence | root
    (2 rows)

    archdb=# select * from users;
    id |     name     |       email       |                        password_hash                         | role
    ----+--------------+-------------------+--------------------------------------------------------------+-------
    1 | Steve Normis | normis@gmail.com  | $2b$12$ehiJwcwllOtLTP37HbqaVOQhT5IjILUSRzxnI8lYfTmWpyaoiXeyW | user
    2 | John Doe     | base_user@ml.com  | $2b$12$kB.4HtHr.EUT7.gSCVthyelqiJq5Gbw.DlnM0lQSXCtmZVaQyu66e | admin
    3 | Steve Normis | normis2@gmail.com | $2b$12$1rki57jdiiMwdYk7sviQueQhYHwiWyf1IRJV3P6eCM16a4vrPKB6S | user
    4 | John Admin   | admin@admin.ru    | $2b$12$UYArW2ZST70eixnvzwGKpORCvJs1G8Nj.YXt00GYkkQxfgt983S/. | admin
    (4 rows)

    archdb=#
```

<br>
2. Должен быть создан скрипт по созданию базы данных и таблиц, а также
наполнению СУБД тестовыми значениями. Он должен запускаться при первом
запуске вашего сервиса;
<br>
✅ Выполнено <br>
Скрипт создан в файле database.py
<br>
3. Для сущности, должны быть созданы запросы к БД (CRUD) согласно ранее
разработанной архитектуре
<br>
✅ Выполнено <br>
Файл находится в user_api_service/repositories/user_repository.py
<br>
4. Данные о пользователе должны включать логин и пароль. Пароль должен
храниться в закрытом виде (хэширован) – в этом задании опционально
<br>
✅ Выполнено <br>
Файл находится в user_api_service/repositories/user_repository.py
<br>
5. Должно применяться индексирования по полям, по которым будет
производиться поиск
<br>
✅ Выполнено <br>
индексирование по полю email
<br>
6. При необходимости актуализируйте модель архитектуры в Structurizr DSL
<br>
✅ Выполнено
<br>
7. Ваши сервисы должны запускаться через docker-compose командой dockercompose up (создайте Docker файлы для каждого сервиса)
<br>
✅ Выполнено
<br>
