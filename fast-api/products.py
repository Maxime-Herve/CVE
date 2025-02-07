from fastapi import APIRouter

router = APIRouter()

@router.get("/product")
def product_hello():
    return {"Product": "Hello2"}
