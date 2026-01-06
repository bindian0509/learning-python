"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 10: FastAPI Introduction
=============================================================================
Topics: FastAPI basics, routes, request/response, Pydantic models

To run this file:
    pip install fastapi uvicorn
    uvicorn 10_fastapi_intro:app --reload

Then visit: http://localhost:8000/docs for interactive API documentation
=============================================================================
"""

from fastapi import FastAPI, HTTPException, Query, Path, Body, Depends
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

# =============================================================================
# 1. CREATE THE APP
# =============================================================================

app = FastAPI(
    title="Python Crash Course API",
    description="Learning FastAPI basics",
    version="1.0.0"
)


# =============================================================================
# 2. BASIC ROUTES
# =============================================================================

@app.get("/")
async def root():
    """Root endpoint - returns welcome message."""
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello/{name}")
async def hello(name: str):
    """Path parameter example."""
    return {"message": f"Hello, {name}!"}


# =============================================================================
# 3. HTTP METHODS
# =============================================================================

# In-memory "database"
items_db: dict = {}

@app.get("/items")
async def list_items():
    """GET - List all items."""
    return {"items": list(items_db.values())}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """GET - Get single item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.post("/items")
async def create_item(name: str, price: float):
    """POST - Create a new item."""
    item_id = len(items_db) + 1
    items_db[item_id] = {"id": item_id, "name": name, "price": price}
    return items_db[item_id]

@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str, price: float):
    """PUT - Update an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = {"id": item_id, "name": name, "price": price}
    return items_db[item_id]

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """DELETE - Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = items_db.pop(item_id)
    return {"message": "Deleted", "item": deleted}


# =============================================================================
# 4. QUERY PARAMETERS
# =============================================================================

@app.get("/search")
async def search_items(
    q: str,                                    # Required query param
    skip: int = 0,                             # Optional with default
    limit: int = Query(default=10, le=100),    # With validation
    sort_by: Optional[str] = None              # Optional, can be None
):
    """
    Search items with query parameters.

    Example: /search?q=laptop&skip=0&limit=5&sort_by=price
    """
    return {
        "query": q,
        "skip": skip,
        "limit": limit,
        "sort_by": sort_by
    }


# =============================================================================
# 5. PATH PARAMETERS WITH VALIDATION
# =============================================================================

class ItemCategory(str, Enum):
    """Enum for item categories."""
    electronics = "electronics"
    clothing = "clothing"
    food = "food"

@app.get("/categories/{category}")
async def get_by_category(
    category: ItemCategory,
    item_id: int = Path(..., ge=1, le=10000, description="Item ID must be 1-10000")
):
    """
    Get item by category with path validation.

    Category must be one of: electronics, clothing, food
    """
    return {"category": category.value, "item_id": item_id}


# =============================================================================
# 6. PYDANTIC MODELS - REQUEST BODY
# =============================================================================

class ItemCreate(BaseModel):
    """Model for creating an item."""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)
    category: ItemCategory
    tags: List[str] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Laptop",
                    "description": "A powerful laptop",
                    "price": 999.99,
                    "quantity": 10,
                    "category": "electronics",
                    "tags": ["tech", "portable"]
                }
            ]
        }
    }

class ItemResponse(BaseModel):
    """Model for item response."""
    id: int
    name: str
    description: Optional[str]
    price: float
    quantity: int
    category: ItemCategory
    tags: List[str]
    created_at: datetime

# Better items database
items_v2_db: dict = {}

@app.post("/v2/items", response_model=ItemResponse)
async def create_item_v2(item: ItemCreate):
    """Create item using Pydantic model."""
    item_id = len(items_v2_db) + 1

    db_item = ItemResponse(
        id=item_id,
        created_at=datetime.now(),
        **item.model_dump()
    )

    items_v2_db[item_id] = db_item
    return db_item


# =============================================================================
# 7. RESPONSE MODELS
# =============================================================================

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str  # Included when creating

class UserResponse(UserBase):
    id: int
    is_active: bool = True
    # password NOT included in response!

users_db: dict = {}

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    """
    Create user - notice password is NOT in response.
    response_model filters the output.
    """
    user_id = len(users_db) + 1
    db_user = {
        "id": user_id,
        "email": user.email,
        "username": user.username,
        "password": user.password,  # Stored but not returned
        "is_active": True
    }
    users_db[user_id] = db_user
    return db_user  # FastAPI filters to UserResponse


# =============================================================================
# 8. ERROR HANDLING
# =============================================================================

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Demonstrate error handling."""
    if user_id not in users_db:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found",
            headers={"X-Error": "User not found"}
        )
    return users_db[user_id]


# =============================================================================
# 9. DEPENDENCIES (Dependency Injection)
# =============================================================================

async def get_db():
    """Dependency that provides database connection."""
    # In real app: yield database session
    db = {"connection": "active"}
    try:
        yield db
    finally:
        # Cleanup
        pass

async def verify_api_key(api_key: str = Query(...)):
    """Dependency that validates API key."""
    if api_key != "secret123":
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

@app.get("/protected")
async def protected_route(
    db: dict = Depends(get_db),
    api_key: str = Depends(verify_api_key)
):
    """Route with dependencies."""
    return {
        "message": "Access granted",
        "db_status": db["connection"],
        "api_key": api_key
    }


# =============================================================================
# 10. ASYNC VS SYNC
# =============================================================================

import time
import asyncio

@app.get("/sync-endpoint")
def sync_endpoint():
    """
    Sync endpoint - use for CPU-bound or blocking operations.
    FastAPI runs this in a thread pool.
    """
    time.sleep(0.1)  # Blocking operation
    return {"type": "sync", "message": "This ran in a thread pool"}

@app.get("/async-endpoint")
async def async_endpoint():
    """
    Async endpoint - use for I/O-bound operations.
    Runs in the main async loop.
    """
    await asyncio.sleep(0.1)  # Non-blocking
    return {"type": "async", "message": "This ran in the async loop"}


# =============================================================================
# 11. MULTIPLE REQUEST BODY PARAMETERS
# =============================================================================

class Product(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    product: Product
    quantity: int
    notes: Optional[str] = None

@app.post("/orders")
async def create_order(
    order: Order,
    priority: int = Body(default=1, ge=1, le=5),
    customer_id: int = Body(...)
):
    """Multiple body parameters."""
    return {
        "order": order.model_dump(),
        "priority": priority,
        "customer_id": customer_id
    }


# =============================================================================
# 12. CORS (Cross-Origin Resource Sharing)
# =============================================================================

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =============================================================================
# RUNNING THE APP
# =============================================================================

# To run this application:
#
# 1. Install dependencies:
#    pip install fastapi uvicorn
#
# 2. Run with uvicorn:
#    uvicorn 10_fastapi_intro:app --reload
#
# 3. Open in browser:
#    - API: http://localhost:8000
#    - Interactive docs: http://localhost:8000/docs
#    - Alternative docs: http://localhost:8000/redoc

if __name__ == "__main__":
    import uvicorn
    print("""
=============================================================================
FastAPI Crash Course Application
=============================================================================

To run this application, use one of these methods:

Method 1 - uvicorn command:
    uvicorn 10_fastapi_intro:app --reload

Method 2 - Run this file directly:
    python 10_fastapi_intro.py

Then visit:
    http://localhost:8000        - Root endpoint
    http://localhost:8000/docs   - Interactive API documentation (Swagger)
    http://localhost:8000/redoc  - Alternative documentation (ReDoc)

=============================================================================
""")
    uvicorn.run(app, host="0.0.0.0", port=8000)

