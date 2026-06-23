from fastapi import FastAPI

from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Catalog API"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "API Running Successfully"
    }