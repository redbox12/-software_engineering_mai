from database import create_product, products  

def seed_demo_products() -> None:
    """Заполняет MongoDB 10-ю тестовыми товарами (id будут присвоены автоматически)."""
    if products.estimated_document_count() > 0:
        return                                 

    demo_items = [
        # admin_id = 1
        {"name": "Зубная паста Parodontax",          "price": 200,  "description": "Лучшая паста в мире",           "admin_id": 1},
        {"name": "Зубная нить Colgate",              "price": 150,  "description": "30 м восковой нити",           "admin_id": 1},
        {"name": "Щётка Oral-B Pro Expert",          "price": 320,  "description": "Средняя жёсткость щетины",      "admin_id": 1},
        {"name": "Шампунь Head&Shoulders Classic",   "price": 390,  "description": "400 мл против перхоти",         "admin_id": 1},
        {"name": "Гель для душа AXE Dark Temptation","price": 270,  "description": "Шоколадный аромат, 250 мл",     "admin_id": 1},

        # admin_id = 2
        {"name": "Крем Nivea Soft",                  "price": 210,  "description": "Увлажнение, банка 75 мл",       "admin_id": 2},
        {"name": "Дезодорант Rexona Cobalt",         "price": 230,  "description": "48 ч защиты, 150 мл",           "admin_id": 2},
        {"name": "Бальзам для губ Carmex Classic",   "price": 260,  "description": "Тюбик 10 г, SPF 15",            "admin_id": 2},
        {"name": "Мыло туалетное Dove Beauty Bar",   "price":  95,  "description": "¼ крема, 100 г",               "admin_id": 2},
        {"name": "Лосьон после бритья Gillette Cool","price": 420,  "description": "Освежающий эффект, 100 мл",     "admin_id": 2},
    ]

    for item in demo_items:
        admin_id = item.pop("admin_id")
        create_product(item, admin_id)
    print("MongoDB заполнена тестовыми товарами.")
