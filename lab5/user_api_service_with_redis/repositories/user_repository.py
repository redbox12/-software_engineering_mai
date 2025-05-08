from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate
from redis_cache import RedisCache

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        self.cache = RedisCache()

    def create(self, user: UserCreate, password_hash: str, role: str) -> User:
        db_user = User(
            email=user.email,
            name=user.name,
            password_hash=password_hash,
            role=role
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        
        # Сохраняем нового пользователя в кеш
        self.cache.set_user(db_user)
        
        # Обновляем кеш всех пользователей
        all_users = self.db.query(User).all()
        self.cache.set_all_users(all_users)
        
        return db_user

    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_all(self) -> list[User]:
        # Пробуем получить из кеша
        cached_users = self.cache.get_all_users()
        if cached_users:
            return cached_users

        # Если нет в кеше, получаем из БД
        users = self.db.query(User).all()
        # Сохраняем в кеш
        self.cache.set_all_users(users)
        return users

    def update(self, email: str, new_name: str = None, new_email: str = None, new_password_hash: str = None) -> bool:
        user = self.get_by_email(email)
        if not user:
            return False

        if new_name:
            user.name = new_name
        if new_email:
            user.email = new_email
        if new_password_hash:
            user.password_hash = new_password_hash

        self.db.commit()
        self.db.refresh(user)
        
        # Обновляем кеш пользователя
        self.cache.set_user(user)
        
        # Обновляем кеш всех пользователей
        all_users = self.db.query(User).all()
        self.cache.set_all_users(all_users)
        
        return True

    def delete_by_email(self, email: str) -> bool:
        user = self.get_by_email(email)
        if not user:
            return False

        self.db.delete(user)
        self.db.commit()
        
        # Удаляем пользователя из кеша
        self.cache.delete_user(user.id)
        
        # Обновляем кеш всех пользователей
        all_users = self.db.query(User).all()
        self.cache.set_all_users(all_users)
        
        return True
