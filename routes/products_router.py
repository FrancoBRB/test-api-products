from fastapi import APIRouter, HTTPException, Response, status
from schemas.product_schema import Product
from uuid import uuid4
from config.database import Conn
from models.product_model import Products
from starlette.status import HTTP_204_NO_CONTENT

products = APIRouter()


@products.get('/products')
def get_products_list():
    return Conn.execute(Products.select()).fetchall()


@products.get('/products/{id}')
def get_product(id: str):
    return Conn.execute(Products.select().where(Products.c.id == id)).first()


@products.post('/products')
def create_product(new_product: Product):
    n_product = {
        "name": new_product.name,
        "description": new_product.description,
        "price": new_product.price
    }
    r = Conn.execute(Products.insert().values(n_product))
    return Conn.execute(Products.select().where(Products.c.id == r.lastrowid)).first()


@products.delete('/products/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: str):
    Conn.execute(Products.delete().where(Products.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@products.put('/products/{id}')
def update_product(id: str, upd_product: Product):
    Conn.execute(Products.update().values(
        name=upd_product.name,
        description=upd_product.description,
        price=upd_product.price
    ).where(Products.c.id == id))
    return Conn.execute(Products.select().where(Products.c.id == id)).first()
