from fastapi import FastAPI
from routes import router
from database import init_db

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
def on_startup():
    init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
