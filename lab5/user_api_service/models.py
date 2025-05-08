from sqlalchemy import Column, Integer, String, CheckConstraint
from database import SessionLocal, engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'user')", name="check_user_role"),
    )
