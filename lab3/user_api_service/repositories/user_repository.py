from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_data: UserCreate, hashed_password: str, role: str):
        user = User(
            name=user_data.name,
            email=user_data.email,
            password_hash=hashed_password,
            role=role
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_by_email(self, email: str):
        user = self.get_by_email(email)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True

    def update(self, email: str, name=None, new_email=None, password_hash=None):
        user = self.get_by_email(email)
        if not user:
            return None
        if name:
            user.name = name
        if new_email:
            user.email = new_email
        if password_hash:
            user.password_hash = password_hash
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all(self):
        return self.db.query(User).all()
