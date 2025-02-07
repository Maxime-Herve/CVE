from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cve_hello():
    response = client.get("/cve")
    assert response.status_code == 200
    assert response.json() == {"CVE": "Hello"}
