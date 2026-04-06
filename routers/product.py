from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models, schemas
from config import settings

router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("", response_model=schemas.ProductListResponse)
def get_products(page: int = 1, db: Session = Depends(get_db)):
    page_size = settings.PAGE_SIZE
    skip = (page - 1) * page_size

    total = db.query(models.Product).count()
    products = db.query(models.Product).offset(skip).limit(page_size).all()

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1) // page_size,
        "data": products
    }

@router.post("", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):

    category = db.query(models.Category).filter(models.Category.id == product.category_id).first()

    if not category:
        raise HTTPException(status_code=400, detail="Invalid category_id")

    db_product = models.Product(**product.dict())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

@router.get("/{id}", response_model=schemas.ProductDetailResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product)\
        .options(joinedload(models.Product.category))\
        .filter(models.Product.id == id)\
        .first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

@router.put("/{id}", response_model=schemas.ProductResponse)
def update_product(id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return db_product

@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}