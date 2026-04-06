from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from config import settings

router = APIRouter(prefix="/api/categories", tags=["Categories"])

@router.get("", response_model=schemas.CategoryListResponse)
def get_categories(page: int = 1, db: Session = Depends(get_db)):
    page_size = settings.PAGE_SIZE
    skip = (page - 1) * page_size

    total = db.query(models.Category).count()
    categories = db.query(models.Category).offset(skip).limit(page_size).all()

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1) // page_size,
        "data": categories
    }

@router.post("", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Category).filter(models.Category.name == category.name).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Category already exists"
        )

    db_category = models.Category(**category.model_dump())

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category

@router.get("/{id}", response_model=schemas.CategoryResponse)
def get_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category

@router.put("/{id}", response_model=schemas.CategoryResponse)
def update_category(id: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.id == id).first()

    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)

    return db_category

@router.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()

    return {"message": "Category deleted successfully"}