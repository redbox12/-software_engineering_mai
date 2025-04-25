from fastapi import FastAPI

from routes import router
from seed import seed_demo_products   # ← импорт функции, которую мы создали

app = FastAPI(title="Marketplace API")

# ─── однократное заполнение MongoDB тестовыми товарами ────────────────────────
@app.on_event("startup")
async def fill_demo_data() -> None:
    seed_demo_products()              # если коллекция products пуста, добавит 10 позиций

# ─── подключаем все эндпоинты ─────────────────────────────────────────────────
app.include_router(router)

# ─── локальный запуск (docker-образ и так запускает uvicorn) ─────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
