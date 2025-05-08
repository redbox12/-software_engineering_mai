from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import UserCreate, UserLogin, UserUpdate, UserCreateAdmin, UserOut
from repositories.user_repository import UserRepository
from auth import hash_password, verify_password, create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def register_user(user: UserCreate, role: str, db: Session):
    repo = UserRepository(db)
    if repo.get_by_email(user.email):
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    hashed = hash_password(user.password)
    repo.create(user, hashed, role)
    return {"message": "Вы зарегистрированы"}

@router.post("/api/v1/user/create", tags=["Регистрация"])
def register_regular_user(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, "user", db)

@router.post("/api/v1/admin/create", tags=["Регистрация"])
def register_admin_user(user: UserCreateAdmin, db: Session = Depends(get_db)):
    return register_user(user, "admin", db)

@router.post("/api/v1/login", tags=["Авторизация"])
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    db_user = repo.get_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Неверные данные")
    token = create_access_token(db_user.email, db_user.role, db_user.id)
    return {"access_token": token, "token_type": "Bearer"}

@router.delete("/api/v1/user/delete", tags=["Пользователь"])
def delete_user(email: str, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    if repo.delete_by_email(email):
        return {"message": "Пользователь удалён"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@router.put("/api/v1/user/update", tags=["Пользователь"])
def update_user(user: UserUpdate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    password_hash = hash_password(user.new_password) if user.new_password else None
    updated = repo.update(user.email, user.new_name, user.new_email, password_hash)
    if updated:
        return {"message": "Обновление выполнено"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@router.get("/api/v1/user/get_all", response_model=list[UserOut], tags=["Пользователь"])
def get_all_users(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.get_all()
