## 🧪 Лабораторная работа №5
**📚 Предмет: Программная инженерия** <br>
**👨‍💻 Выполнил: Королев Иван, М80-114СВ**

### 📋 Задание:
1.  Для данных, хранящихся в реляционной базе PotgreSQL реализуйте шаблон
сквозное чтение и сквозная запись (Пользователь/Клиент …);
2.  В качестве кеша – используйте Redis
3.  Замерьте производительность запросов на чтение данных с и без кеша с
использованием утилиты wrk https://github.com/wg/wrk изменяя количество
потоков из которых производятся запросы (1, 5, 10)
4. Актуализируйте модель архитектуры в Structurizr DSL
5.  Ваши сервисы должны запускаться через docker-compose командой dockercompose up (создайте Docker файлы для каждого сервиса)

### Рекомендации по C++
- Используйте фреймворк Poco https://docs.pocoproject.org/current/
- Пример по работе с Poco Web Servers и Redis
https://github.com/DVDemon/arch_lecture_examples/tree/main/hl_mai_lab_05

### Рекомендации по Python:
- Используйте FastAPI для построения интерфейсов
- Простой пример применения redis
https://github.com/DVDemon/architecture_python/tree/main/07_redis

## Запуск программы

```bash
docker-compose up --build
```

## 📊 Тест производительности

### 🎯 Тестируемый эндпоинт
`/api/v1/user/get_all` - эндпоинт чтения данных.

### 📈 Результаты тестов

#### 🔄 1 поток (без Redis)
```bash
Running 10s test @ http://localhost:8001/api/v1/user/get_all
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    67.56ms   66.07ms 532.26ms   94.09%
    Req/Sec    18.63      3.77    20.00     88.12%
  191 requests in 10.83s, 50.11KB read
Requests/sec:     17.64
Transfer/sec:      4.63KB
```

#### 🔄 1 поток (с Redis)
```bash
Running 10s test @ http://localhost:8001/api/v1/user/get_all
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    51.81ms    5.14ms  60.62ms   79.27%
    Req/Sec    19.29      2.56    20.00     93.00%
  193 requests in 10.01s, 50.63KB read
Requests/sec:     19.27
Transfer/sec:      5.06KB
```

#### 🔄 5 потоков (без Redis)
```bash
Running 10s test @ http://localhost:8001/api/v1/user/get_all
  5 threads and 5 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    62.41ms   10.48ms 129.55ms   67.12%
    Req/Sec    15.99      4.91    20.00     60.00%
  800 requests in 10.01s, 209.99KB read
Requests/sec:     79.90
Transfer/sec:     20.97KB
```

#### 🔄 5 потоков (с Redis)
```bash
Running 10s test @ http://localhost:8001/api/v1/user/get_all
  5 threads and 5 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    62.07ms   10.73ms  99.25ms   59.70%
    Req/Sec    16.06      4.89    20.00     60.80%
  804 requests in 10.02s, 211.04KB read
Requests/sec:     80.26
Transfer/sec:     21.07KB
```

#### 🔄 10 потоков (без Redis)
```bash
Running 10s test @ http://localhost:8001/api/v1/user/get_all
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    88.57ms   79.79ms 565.57ms   93.25%
    Req/Sec    14.28      5.27    20.00     52.82%
  1460 requests in 10.90s, 382.72KB read
Requests/sec:    133.90
Transfer/sec:     35.10KB
```

#### 🔄 10 потоков (с Redis)
```bash
Running 10s test @ http://localhost:8001/api/v1/user/get_all
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   104.17ms  131.97ms   1.18s    92.42%
    Req/Sec    14.25      5.31    20.00     53.35%
  1445 requests in 11.14s, 379.17KB read
Requests/sec:    129.75
Transfer/sec:     34.05KB
```

## 💻 Характеристики тестового окружения:

### 🖥️ Процессор:
- Intel Core i7-1065G7
- 4 ядра, 8 потоков (Hyper-Threading)
- Частота: 1.30 GHz
- 8 GB ОЗУ


### 🧪 Тестирование:
- Инструмент: wrk
- Тестируемый эндпоинт: `/api/v1/user/get_all`
- Длительность теста: 10 секунд
- Количество потоков: 1, 5, 10

#### 📝 Команды для тестирования:

1. Тест с 1 потоком:
```bash
wrk -t1 -c1 -d10s http://localhost:8001/api/v1/user/get_all
```


2. Тест с 5 потоками:
```bash
wrk -t5 -c5 -d10s http://localhost:8001/api/v1/user/get_all
```


3. Тест с 10 потоками:
```bash
wrk -t10 -c10 -d10s http://localhost:8001/api/v1/user/get_all
```

## Результаты
1. Для данных, хранящихся в реляционной базе PotgreSQL реализуйте шаблон сквозное чтение и сквозная запись (Пользователь/Клиент …);
✅ Выполнено
Реализовано в сервисе user_api_service:
- Создание пользователя (POST /api/v1/admin/create)
- Получение пользователя (GET /api/v1/user/{user_id})
- Получение всех пользователей (GET /api/v1/user/get_all)
- Обновление пользователя (PUT /api/v1/user/{user_id})
- Удаление пользователя (DELETE /api/v1/user/{user_id})

2. В качестве кеша – используйте Redis
✅ Выполнено
Контейнер с Redis в docker-compose.yaml:
```yaml
  redis:
    image: redis:latest
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5
```

3. Замерьте производительность запросов на чтение данных с и без кеша с использованием утилиты wrk
✅ Выполнено
Результаты тестирования:
смотреть выше в разделе `Тест производительности`

4. Актуализируйте модель архитектуры в Structurizr DSL
✅ Выполнено


5. Ваши сервисы должны запускаться через docker-compose командой docker-compose up
✅ Выполнено <br>

Команда для запуска:
```bash
docker-compose up --build
```

Дополнительно реализовано:
✅ Скрипт для проверки данных в Redis:
- lab5/user_api_service_with_redis/check_redis.py
- Позволяет просматривать данные в кеше
