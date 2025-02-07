from fastapi import APIRouter

router = APIRouter()

@router.get("/cve")
def cve_hello():
    return {"CVE": "Hello"}
