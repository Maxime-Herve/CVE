from fastapi import APIRouter, HTTPException, Query
import requests
from requests.auth import HTTPBasicAuth

router = APIRouter()

username = "maxime.herve@etu.mines-ales.fr"
password = "T*fFDSUY3@LQ0O"

@router.get("/vendors/{vendor_name}")
def get_vendor_info(vendor_name: str):
    url = f"https://app.opencve.io/api/vendors/{vendor_name}"

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        return response.json()

    raise HTTPException(status_code=response.status_code, detail=response.json())

@router.get("/vendors/{vendor_name}/cve")
def get_vendor_cve(vendor_name: str, page: int = Query(None, description="Page number for pagination")):
    if page:
        url = f"https://app.opencve.io/api/vendors/{vendor_name}/cve?page={page}"
    else:
        url = f"https://app.opencve.io/api/vendors/{vendor_name}/cve" 

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        return response.json()

    raise HTTPException(status_code=response.status_code, detail=response.json())

@router.get("/vendors/{vendor_name}/products/{product_name}")
def get_product_info(vendor_name: str, product_name: str):
    url = f"https://app.opencve.io/api/vendors/{vendor_name}/products/{product_name}"

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        return response.json()

    raise HTTPException(status_code=response.status_code, detail=response.json())

@router.get("/vendors/{vendor_name}/products/{product_name}/cve")
def get_product_cve(vendor_name: str, product_name: str, page: int = Query(None, description="Page number for pagination")):
    if page:
        url = f"https://app.opencve.io/api/vendors/{vendor_name}/products/{product_name}/cve?page={page}"
    else:
        url = f"https://app.opencve.io/api/vendors/{vendor_name}/products/{product_name}/cve" 

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        return response.json()

    raise HTTPException(status_code=response.status_code, detail=response.json())
