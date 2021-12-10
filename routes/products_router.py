from fastapi import APIRouter, HTTPException
from schemas.product_schema import Product
from uuid import uuid4

products = APIRouter()

"""
Only for testing propuse i'll save json data into array.
Eventually the array will be replaced by SQL table.
"""
products_array = []


@products.get('/products')
def get_products_list():
    return products_array


@products.get('/products/{id}')
def get_product(id: str):
    for prdct in products_array:
        if prdct["id"] == id:
            return prdct
    raise HTTPException(status_code=404, detail="Product not found.")


@products.post('/products')
def create_product(new_product: Product):
    new_product.id = str(uuid4())
    n_product = new_product.dict()
    products_array.append(n_product)
    return products_array[-1]  # Index -1 reference to last date added


@products.delete('/products/{id}')
def update_product(id: str):
    for index, prdct in enumerate(products_array):
        if prdct["id"] == id:
            products_array.pop(index)
            return {"message": "Product has been sucessfuly deleted."}
    raise HTTPException(status_code=404, detail="Product not found.")


@products.put('/products/{id}')
def delete_product(id: str, upd_product: Product):
    for index, prdct in enumerate(products_array):
        if prdct["id"] == id:
            products_array[index]["name"] = upd_product.name
            products_array[index]["description"] = upd_product.description
            products_array[index]["price"] = upd_product.price
            return {"message": "Product has been sucessfuly updated."}
    raise HTTPException(status_code=404, detail="Product not found.")
