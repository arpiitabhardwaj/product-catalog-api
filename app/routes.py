from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import Product

router = APIRouter()

@router.get("/products")
def get_products(
    limit: int = 20,
    category: str = None,
    cursor: int = None,
    db: Session = Depends(get_db)
):

    query = db.query(Product)

    if category:
        query = query.filter(
            Product.category == category
        )

    if cursor:
        query = query.filter(
            Product.id < cursor
        )

    products = (
        query
        .order_by(Product.id.desc())
        .limit(limit)
        .all()
    )

    next_cursor = None

    if products:
        next_cursor = products[-1].id

    return {
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "category": p.category,
                "price": p.price
            }
            for p in products
        ],
        "next_cursor": next_cursor
    }