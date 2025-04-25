from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import traceback

DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "archdb"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db():
    try:
        with engine.connect() as conn:
            print("🔧 Проверяем наличие таблицы users...")

            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    role TEXT NOT NULL CHECK (role IN ('admin', 'user'))
                );
            """))
            print("Таблица users готова.")

            conn.execute(text("""
                INSERT INTO users (name, email, password_hash, role) VALUES
                ('John Admin', 'admin@admin.ru', '$2b$12$lm6PMrRM16mJoaZm9GAA3uQl4ZXUS4LlrVOZrf/VVKQvBo2sJxbtu', 'admin')
                ON CONFLICT (id) DO NOTHING;
            """))

            conn.execute(text("""
                INSERT INTO users (name, email, password_hash, role) VALUES
                ('Steve Normis', 'normis@gmail.com', '$2b$12$ehiJwcwllOtLTP37HbqaVOQhT5IjILUSRzxnI8lYfTmWpyaoiXeyW', 'user')
                ON CONFLICT (id) DO NOTHING;
            """))

            conn.commit()
            print("Тестовые пользователи добавлены (если нужно).")

    except SQLAlchemyError as e:
        print("Ошибка при инициализации базы данных:")
        print(e)
        traceback.print_exc()
