import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from faker import Faker
from random import choice, uniform
from datetime import datetime

from app.database import SessionLocal
from app.models import Product

fake = Faker()

db = SessionLocal()

categories = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home"
]

products = []

for i in range(200000):
    products.append(
        Product(
            name=fake.word(),
            category=choice(categories),
            price=round(uniform(100, 5000), 2),
            created_at=datetime.now()
        )
    )

    if (i + 1) % 10000 == 0:
        print(f"{i + 1} products prepared")

db.bulk_save_objects(products)
db.commit()
db.close()

print("200000 products inserted successfully")