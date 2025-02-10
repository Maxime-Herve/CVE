import requests
from requests.auth import HTTPBasicAuth
import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/filtering")
async def filtering(vendor: str, product: str):

    base_api_url = "https://app.opencve.io/api/cve"
    username = os.getenv('API_USERNAME')
    password = os.getenv('API_PASSWORD')
    response = requests.get(base_api_url + "?vendor" + vendor + "&product=" + product , auth=HTTPBasicAuth(username, password))

    return {"Filtering": response.json()}

