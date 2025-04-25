from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user, is_admin
from models import ProductCreate, ProductUpdate, ProductOut
from database import (
    list_products,
    create_product,
    get_product,
    update_product,
    delete_product,
)

router = APIRouter()


@router.get("/api_marketplace/v1/user/hello", tags=["Проверка обычного пользователя"])
def user_hello(user: dict = Depends(get_current_user)):
    return {"message": f"Привет, {user['email']}!"}


@router.get("/api_marketplace/v1/admin/hello",  tags=["Проверка админ пользователя"])
def admin_hello(admin: dict = Depends(is_admin)):
    return {"message": f"Привет, {admin['email']}! Это страница администраторов."}


@router.post(
    "/api_marketplace/v1/admin/product",
    response_model=ProductOut,
    status_code=201,
    tags=["Товары"],
)
def create_product_route(
    product: ProductCreate, admin: dict = Depends(is_admin)
):
    res = create_product(product.dict(), admin["id"])
    if "error" in res:
        raise HTTPException(400, res["error"])
    return res["product"]


@router.get("/api_marketplace/v1/products", tags=["Товары"], response_model=list[ProductOut])
def list_products_route():
    return list_products()


@router.get("/api_marketplace/v1/products/{product_id}", tags=["Товары"], response_model=ProductOut)
def get_product_route(product_id: int):
    prod = get_product(product_id)
    if not prod:
        raise HTTPException(404, "Товар не найден")
    return prod


@router.put("/api_marketplace/v1/products/{product_id}", tags=["Товары"], response_model=ProductOut)
def update_product_route(
    product_id: int,
    product: ProductUpdate,
    admin: dict = Depends(is_admin),
):
    res = update_product(product_id, product.dict(exclude_unset=True))
    if "error" in res:
        raise HTTPException(404, res["error"])
    return res["product"]


@router.delete("/api_marketplace/v1/products/{product_id}", tags=["Товары"])
def delete_product_route(product_id: int, admin: dict = Depends(is_admin)):
    res = delete_product(product_id)
    if "error" in res:
        raise HTTPException(404, res["error"])
    return {"message": res["message"]}
