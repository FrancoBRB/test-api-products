from pydantic import BaseModel
from typing import Optional, Text


class Product(BaseModel):
    id: Optional[str]
    name: str
    description: Text
    price: int
