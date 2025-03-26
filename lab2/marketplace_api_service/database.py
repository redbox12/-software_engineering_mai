import json
from pathlib import Path

MARKETPLACE_DB_FILE = Path("MARKETPLACE_DB.json")  #БД markertplace JSON-файл

def load_products():
    """Загружает товары из JSON-файла"""
    if not MARKETPLACE_DB_FILE.exists():
        return []
    try:
        with open(MARKETPLACE_DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Ошибка чтения файла marketplace.json: некорректный формат JSON")

def save_products(products):
    """Сохраняет товары в JSON-файл"""
    try:
        with open(MARKETPLACE_DB_FILE, "w", encoding="utf-8") as f:
            json.dump(products, f, indent=4, ensure_ascii=False)
    except Exception as e:
        raise IOError(f"Ошибка сохранения файла marketplace.json: {e}")

def create_product(product, admin_id):
    """Создает товар и добавляет его в marketplace.json"""
    try:
        products = load_products()  # Загружаем существующие товары

        # Проверяем, существует ли похожий товар
        for existing_product in products:
            if existing_product["name"] == product["name"] and existing_product["price"] == product["price"]:
                return {"error": "Товар с таким именем и ценой уже существует"}

        # Присваиваем ID и admin_id новому товару
        product["id"] = len(products) + 1
        product["admin_id"] = admin_id

        # Добавляем новый товар и сохраняем
        products.append(product)
        save_products(products)
        return {"message": "Товар успешно добавлен", "product": product}
    except ValueError as ve:
        return {"error": f"Ошибка загрузки товаров: {ve}"}
    except IOError as ioe:
        return {"error": f"Ошибка сохранения товаров: {ioe}"}
    except Exception as e:
        return {"error": f"Неизвестная ошибка: {e}"}
    
def delete_product(product_id: int):
    """Удаляет товар из marketplace.json по его ID"""
    try:
        products = load_products()  # Загружаем существующие товары

        # Проверяем, существует ли товар с таким ID
        product_to_delete = next((product for product in products if product["id"] == product_id), None)
        if not product_to_delete:
            return {"error": f"Товар с ID {product_id} не найден"}

        # Удаляем товар
        products = [product for product in products if product["id"] != product_id]
        save_products(products)  # Сохраняем обновленный список товаров

        return {"message": f"Товар с ID {product_id} успешно удален"}
    except IOError as ioe:
        return {"error": f"Ошибка при удалении товара: {ioe}"}
    except Exception as e:
        return {"error": f"Неизвестная ошибка: {e}"}
    
def update_product(product_id: int, updated_data: dict):
    """Обновляет товар в marketplace.json по его ID"""
    try:
        products = load_products()  # Загружаем существующие товары

        # Найти товар с указанным ID
        product_to_update = next((product for product in products if product["id"] == product_id), None)
        if not product_to_update:
            return {"error": f"Товар с ID {product_id} не найден"}

        # Обновляем данные товара
        for key, value in updated_data.items():
            if key in product_to_update:  # Обновляем только существующие поля
                product_to_update[key] = value

        save_products(products)  # Сохраняем обновленный список товаров
        return {"message": f"Товар с ID {product_id} успешно обновлен", "product": product_to_update}
    except IOError as ioe:
        return {"error": f"Ошибка при обновлении товара: {ioe}"}
    except Exception as e:
        return {"error": f"Неизвестная ошибка: {e}"}