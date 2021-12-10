from sqlalchemy import Table, Column
from config.database import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String, Text

from schemas.product_schema import Product

Products = Table("products", meta,
                 Column("id", Integer, primary_key=True),
                 Column("name", String(255)),
                 Column("description", Text),
                 Column("price", Integer)
                 )

meta.create_all(engine)
