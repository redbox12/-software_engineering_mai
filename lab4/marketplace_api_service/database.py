import os
from typing import Dict, List, Any

from bson import ObjectId
from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError

# ─── подключение ───────────────────────────────────────────────────────────────
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo_db:27017")
DB_NAME   = os.getenv("MONGO_DB",  "marketplace")

client: MongoClient = MongoClient(MONGO_URI)
db                  = client[DB_NAME]
products            = db["products"]

# индексы
products.create_index([("id", ASCENDING)],    unique=True, name="id_uq")
products.create_index(
    [("name", ASCENDING), ("price", ASCENDING)],
    unique=True,
    name="name_price_uq",
)

# ─── вспомогательные функции ───────────────────────────────────────────────────
def _next_id() -> int:
    """Получить следующий целочисленный id."""
    last = products.find_one(sort=[("id", -1)], projection={"id": 1})
    return (last["id"] if last else 0) + 1


def to_client(doc: Dict[str, Any]) -> Dict[str, Any]:
    """Готовит Mongo-документ к отдаче наружу (ObjectId → str)."""
    if not doc:
        return doc
    doc = doc.copy()
    doc["id"] = int(doc["id"])
    doc["_id"] = str(doc["_id"])
    return doc


# ─── CRUD ──────────────────────────────────────────────────────────────────────
def create_product(data: Dict[str, Any], admin_id: int) -> Dict[str, Any]:
    data["id"]       = _next_id()
    data["admin_id"] = admin_id
    try:
        ins = products.insert_one(data)
        return {"product": to_client(products.find_one({"_id": ins.inserted_id}))}
    except DuplicateKeyError:
        return {"error": "Товар с таким именем и ценой уже существует"}


def list_products() -> List[Dict[str, Any]]:
    return [to_client(d) for d in products.find()]


def get_product(product_id: int) -> Dict[str, Any] | None:
    doc = products.find_one({"id": product_id})
    return to_client(doc) if doc else None


def update_product(product_id: int, updated: Dict[str, Any]) -> Dict[str, Any]:
    if not updated:
        return {"error": "Нет данных для обновления"}

    res = products.update_one({"id": product_id}, {"$set": updated})
    if res.matched_count == 0:
        return {"error": f"Товар с ID {product_id} не найден"}

    return {"product": to_client(products.find_one({"id": product_id}))}


def delete_product(product_id: int) -> Dict[str, str]:
    res = products.delete_one({"id": product_id})
    if res.deleted_count == 0:
        return {"error": f"Товар с ID {product_id} не найден"}
    return {"message": f"Товар с ID {product_id} успешно удалён"}
