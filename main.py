from fastapi import FastAPI
from routes.products_router import products


app = FastAPI()
app.include_router(products)

@app.get('/')
def welcome():
    return {"message":"Welcome to my api for test propouse.",
            "auth":"Authorized for read only, if you want to write u need to type the password."}
