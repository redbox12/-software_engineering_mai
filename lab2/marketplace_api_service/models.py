from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., example="Зубная паста. Parodontax")
    price: float = Field(..., example= 200.00)
    description: str = Field(..., example="Лучшая паста в мире. Состав: ... Способ применения: ...")
    
class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Обновленное название товара")
    price: Optional[float] = Field(None, example=250.00)
    description: Optional[str] = Field(None, example="Обновленное описание товара")