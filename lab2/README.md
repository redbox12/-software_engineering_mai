## Лабораторная работа №2 
**Предмет: Программная инженерия** <br>
**Выполнил: Королев Иван, М80-114СВ**

1. Создайте HTTP REST API для сервисов, спроектированных в первом задании (по
проектированию). Должно быть реализовано как минимум два сервиса
(управления пользователем, и хотя бы один «бизнес» сервис)

2. Сервис должен поддерживать аутентификацию с использованием JWT-token
(Bearer)
3. Должен быть отдельный endpoint для получения токена по логину/паролю
4. Сервис должен реализовывать как минимум GET/POST методы
5. Данные сервиса должны храниться в памяти (базу данных добавим потом)
6. В целях проверки должен быть заведён мастер-пользователь (имя admin,
пароль secret)
7. Сделайте OpenAPI спецификацию и сохраните ее в корне проекта
8. Актуализируйте модель архитектуры в Structurizr DSL
9. Ваши сервисы должны запускаться через docker-compose коммандой dockercompose up (создайте Docker файлы для каждого сервиса)


## Структура проекта
Проект разделен на два отдельных API:
1. **`user_api` (порт 8001)** – управление пользователями (регистрация, логин, генерация JWT-токенов).
2. **`marketplace_api` (порт 8002)** – проверяет авторизацию, администратор иимеет доступ CRUD операций к товарам интернет магазина

## Дерево проекта
```
/lab2/
├── user_api_service/            # 📂 API управления пользователями
│   ├── main.py                  # Запуск API
│   ├── auth.py                  # Хеширование паролей, JWT
│   ├── database.py              # Работа с JSON-файлом
│   ├── routes.py                # Регистрация и логин
│   ├── models.py                # Pydantic-модели
│   ├── requirements.txt         # Зависимости для user_api_service
│   ├── Dockerfile               # Dockerfile для user_api_service
│
├── marketplace_api_service/     # 📂 API маркетплейса
│   ├── main.py                  # Запуск API
│   ├── auth.py                  # Проверка токена
│   ├── routes.py                # Защищенные маршруты
│   ├── database.py              # Работа с JSON-файлом
│   ├── models.py                # Pydantic-модели
│   ├── requirements.txt         # Зависимости для marketplace_api_service
│   ├── Dockerfile               # Dockerfile для marketplace_api_service
│
│── OpenAPI_marketplace_api_service     # OpenAPI спецификация для marketplace_api_service
│── OpenAPI_user_api_service            # OpenAPI спецификация для user_api_service
│── docker-compose.yaml                 # Конфигурация для запуска сервисов через Docker Compose
```

## Запуск приложения
1. Установите Docker на компьютер
2. После установки, запустите команду:
```
docker-compose up --build
```

##  Обзор приложения
#### 🟢 http://localhost:8001/docs - приложение user_api_service
#### 🟢 http://localhost:8002/docs - приложение marketplace_api_service
<br>

## Результаты

**1. Создайте HTTP REST API для сервисов, спроектированных в первом задании (по
проектированию). Должно быть реализовано как минимум два сервиса
(управления пользователем, и хотя бы один «бизнес» сервис)**
<br>
✅ Было создан сервис управления пользователем: http://localhost:8001/docs - приложение user_api_service <br>
Было создан сервис «бизнес» сервис (СRUD операции товаров для интернет магазина) - http://localhost:8002/docs 
<br>
**2. Сервис должен поддерживать аутентификацию с использованием JWT-token
(Bearer)**
<br>
✅ Поддерживает аутентификацию с использованием JWT-token: http://localhost:8001/docs/api/v1/login
<br>
**3. Должен быть отдельный endpoint для получения токена по логину/паролю**
✅ Поддерживает endpoint для получения токена по логину/паролю: http://localhost:8001/docs/api/v1/login
<br>
**4. Сервис должен реализовывать как минимум GET/POST методы**
<br>
✅ Реализовано в 
<br> 
http://localhost:8001/docs - приложение user_api_service
<br>
http://localhost:8002/docs - приложение marketplace_api_service
<br>
**5. Данные сервиса должны храниться в памяти (базу данных добавим потом)**
<br>
✅ Реализовано
<br>
**6. В целях проверки должен быть заведён мастер-пользователь (имя admin,
пароль secret)**
<br>
✅ Реализовано
<br>
**7. Сделайте OpenAPI спецификацию и сохраните ее в корне проекта**
<br>
✅ Реализовано <br>
│── OpenAPI_marketplace_api_service     # OpenAPI спецификация для marketplace_api_service<br>
│── OpenAPI_user_api_service            # OpenAPI спецификация для user_api_service
<br>
**8. Актуализируйте модель архитектуры в Structurizr DSL**
<br>
✅ Реализовано
<br>
**9. Ваши сервисы должны запускаться через docker-compose коммандой dockercompose up (создайте Docker файлы для каждого сервиса)**
<br>
✅ Реализовано
```
/lab2/
├── user_api_service/            # 📂 API управления пользователями
│    ...
│   ├── Dockerfile               # Dockerfile для user_api_service
│
├── marketplace_api_service/     # 📂 API маркетплейса
│   ...
│   ├── Dockerfile               # Dockerfile для marketplace_api_service
│  ..
│── docker-compose.yaml          # Конфигурация для запуска сервисов через Docker Compose
```
