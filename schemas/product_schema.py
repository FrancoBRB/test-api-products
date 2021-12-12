from pydantic import BaseModel
from typing import Optional, Text


class Product(BaseModel):    
    name: str
    description: Text
    price: int
