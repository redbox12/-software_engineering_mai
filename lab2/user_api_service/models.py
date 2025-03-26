from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str = Field(..., example="Steve Normis")
    email: EmailStr = Field(..., example="normis@gmail.com")
    password: str = Field(..., example="secret")

class UserCreateAdmin(BaseModel):
    name: str = Field(..., example="John Admin")
    email: EmailStr = Field(..., example="admin@admin.ru")
    password: str = Field(..., example="secret")

class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="admin@admin.ru")
    password: str = Field(..., example="secret")

class UserUpdate(BaseModel):
    email: EmailStr = Field(..., example="admin@admin.ru")
    new_name: str = Field(default=None, example="John Doe")
    new_email: EmailStr = Field(default=None, example="base_user@ml.com")
    new_password: str = Field(default=None, example="12345")