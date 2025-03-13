workspace {
    name "Ozon Store"
    !identifiers hierarchical

    model {
        user = person "Покупатель" {
            description "Покупатель интернет-магазина Ozon"
        }

        admin = person "Администратор" {
            description "Администратор магазина, управляющий товарами и пользователями"
        }

        ozonStore = softwareSystem "Система интернет-магазина Ozon" {
            description "Интернет-магазин для покупки товаров"

            apiService = container "API Service" {
                technology "Python / FastAPI"
                description "Backend-сервис, реализующий бизнес-логику"
            }

            database = container "Database" {
                technology "PostgreSQL"
                description "Основная база данных системы"
            }

            paymentService = container "Payment Service" {
                technology "Stripe"
                description "Сервис проведения платежей"
            }

            user -> apiService "Использует магазин через API" "REST/JSON"
            admin -> apiService "Управляет магазином через API" "REST/JSON"
            apiService -> database "SQL-запросы" "POSTGRESQL"
            apiService -> paymentService "Обработка платежей через API" "REST/HTTPS"
        }
    }

    views {
        themes default

        systemContext ozonStore {
            include *
            autolayout lr
        }

        container ozonStore {
            include *
            autolayout lr
        }

        dynamic ozonStore "create_user" "Создание нового пользователя" {
            autoLayout lr
            user -> ozonStore.apiService "POST /api/v1/user/create"
            ozonStore.apiService -> ozonStore.database "Сохраняет данные"
        }

        dynamic ozonStore "search_user_by_login" "Поиск пользователя по логину" {
            autoLayout lr
            admin -> ozonStore.apiService "GET /api/v1/user/search/login"
            ozonStore.apiService -> ozonStore.database "Получает данные пользователя"
        }

        dynamic ozonStore "search_user_by_name" "Поиск пользователя по имени и фамилии" {
            autoLayout lr
            admin -> ozonStore.apiService "POST /api/v1/user/search"
            ozonStore.apiService -> ozonStore.database "Получает данные пользователя"
        }

        dynamic ozonStore "create_product" "Создание товара" {
            autoLayout lr
            admin -> ozonStore.apiService "POST /api/v1/product/create"
            ozonStore.apiService -> ozonStore.database "Сохраняет данные товара"
        }

        dynamic ozonStore "get_products" "Получение списка товаров" {
            autoLayout lr
            user -> ozonStore.apiService "GET /api/v1/products"
            admin -> ozonStore.apiService "GET /api/v1/products"
            ozonStore.apiService -> ozonStore.database "Получает список товаров"
        }

        dynamic ozonStore "add_product_to_cart" "Добавление товара в корзину" {
            autoLayout lr
            user -> ozonStore.apiService "POST /api/v1/cart/add"
            ozonStore.apiService -> ozonStore.database "Проверка и запись товара в корзину"
        }
    }
}
