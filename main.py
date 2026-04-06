from fastapi import FastAPI
from database import engine
import models

from routers import category, product

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Catalog API")

app.include_router(category.router)
app.include_router(product.router)