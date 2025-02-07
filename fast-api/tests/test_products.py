from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_product_hello():
    response = client.get("/product")
    assert response.status_code == 200
    assert response.json() == {"Product": "Hello"}
