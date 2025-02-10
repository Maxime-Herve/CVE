import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cve_hello():
    response = client.get("/cve?vendor=microsoft&product=windows")
    assert response.status_code == 200
    json_response = response.json()
    assert "Filtering" in json_response and json_response["Filtering"] is not None, "Filtering key is missing or has a null value"
