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

for i in range(100):

    product = Product(
        name=fake.word(),
        category=choice(categories),
        price=round(uniform(100, 5000), 2),
        created_at=datetime.now()
    )

    db.add(product)

db.commit()
db.close()

print("100 products inserted successfully")