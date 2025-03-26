from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user, is_admin
from models import ProductCreate, ProductUpdate 
from database import load_products, create_product, delete_product, update_product


router = APIRouter()

@router.get("/api_marketplace/v1/user/hello", tags=["Проверка обычного пользователя"])
def user_hello(user: dict = Depends(get_current_user)):
    return {"message": f"Привет, {user['email']}! Это страница для пользователей."}

@router.get("/api_marketplace/v1/admin/hello", tags=["Проверка продаваца пользователя"])
def admin_hello(admin: dict = Depends(is_admin)):
    return {"message": f"Привет, {admin['email']}! Это страница для администраторов."}

@router.post("/api_marketplace/v1/admin/product", tags=["Товары"])
def create_product_route(product: ProductCreate, admin: dict = Depends(is_admin)):
    """Создает новый продукт в marketplace.json"""
    result = create_product(product.dict(), admin["id"])
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return {"message": f"Продукт {product.name} успешно создан администратором {admin['email']}", "product": result["product"]}

@router.get("/api_marketplace/v1/products", tags=["Товары"])
def get_products():
    """Возвращает список товаров из marketplace.json"""
    products = load_products()
    return products

@router.delete("/api_marketplace/v1/products/{product_id}", tags=["Товары"])
def delete_product_route(product_id: int, admin: dict = Depends(is_admin)):
    """Удаляет товар из marketplace.json по его ID"""
    result = delete_product(product_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return {"message": result["message"]}

@router.put("/api_marketplace/v1/products/{product_id}", tags=["Товары"])
def update_product_route(product_id: int, product: ProductUpdate, admin: dict = Depends(is_admin)):
    """Обновляет товар в marketplace.json по его ID"""
    result = update_product(product_id, product.dict(exclude_unset=True))
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return {"message": result["message"], "product": result["product"]}