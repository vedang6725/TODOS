from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="Electronics")
    description: Optional[str] = Field(None, example="Electronic devices and accessories")
 
 
class CategoryCreate(CategoryBase):
    pass
 
 
class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
 
 
class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
 
    class Config:
        from_attributes = True
 
 
class CategoryListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int
    data: List[CategoryResponse]


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, example="Wireless Headphones")
    description: Optional[str] = Field(None, example="High-quality wireless headphones")
    price: float = Field(..., gt=0, example=49.99)
    stock: int = Field(0, ge=0, example=100)
    category_id: int = Field(..., example=1)
 
 
class ProductCreate(ProductBase):
    pass
 
 
class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    category_id: Optional[int] = None
 
 
class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
 
    class Config:
        from_attributes = True
 
 
class ProductDetailResponse(ProductResponse):
    category: CategoryResponse
 
    class Config:
        from_attributes = True
 
 
class ProductListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int
    data: List[ProductResponse]