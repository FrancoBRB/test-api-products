from fastapi import FastAPI
from routes.products_router import products

app = FastAPI()
app.include_router(products)
