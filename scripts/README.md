# Product Catalog API

## Overview

A backend API built using FastAPI and SQLAlchemy to manage and retrieve product data efficiently.

## Features

* Fetch products using REST API
* Category-based filtering
* Cursor-based pagination
* SQLite database integration
* Bulk product data generation using Faker

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Faker

## Project Structure

codevector-task/

├── app/

│ ├── database.py

│ ├── main.py

│ ├── models.py

│ └── routes.py

├── scripts/

│ └── seed.py

├── requirements.txt

└── README.md

## Installation

Install dependencies:

python -m pip install -r requirements.txt

Run the server:

python -m uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs

## API Endpoints

### GET /

Returns API status.

### GET /products

Returns product list with pagination support.

Query Parameters:

* limit
* category
* cursor

## Sample Response

{
"products": [],
"next_cursor": 81
}

## Future Improvements

* PostgreSQL integration
* Authentication & authorization
* Product creation and update APIs
* Deployment on cloud platforms

## Author

Arpita Bhardwaj
