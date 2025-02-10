import sys
import os
import pytest
from fastapi.testclient import TestClient
from main import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)

def test_get_vendor_info_valid():
    vendor_name = "microsoft"
    response = client.get(f"/vendors/{vendor_name}")

    assert response.status_code == 200
    data = response.json()

    assert 'id' in data
    assert 'created_at' in data
    assert 'updated_at' in data
    assert 'name' in data

def test_get_vendor_info_invalid():
    vendor_name = "microsofttttttttttttttttttt"
    response = client.get(f"/vendors/{vendor_name}")

    assert response.status_code == 404
    data = response.json()

    assert 'detail' in data

def test_get_vendor_cve_valid():
    vendor_name = "microsoft"
    response = client.get(f"/vendors/{vendor_name}/cve")

    assert response.status_code == 200
    data = response.json()

    assert 'count' in data
    assert 'next' in data
    assert 'previous' in data
    assert 'results' in data

def test_get_vendor_cve_invalid():
    vendor_name = "microsoftttttttttttttttttt"
    response = client.get(f"/vendors/{vendor_name}/cve")

    assert response.status_code == 404
    data = response.json()

    assert 'detail' in data

def test_get_vendor_cve_valid_with_page():
    vendor_name = "microsoft"
    response = client.get(f"/vendors/{vendor_name}/cve?page=10")

    assert response.status_code == 200
    data = response.json()

    assert 'count' in data
    assert 'next' in data
    assert 'previous' in data
    assert 'results' in data

def test_get_vendor_cve_invalid_with_page():
    vendor_name = "microsoft"
    response = client.get(f"/vendors/{vendor_name}/cve?page=1000000000")

    assert response.status_code == 404
    data = response.json()

    assert 'detail' in data

def test_get_product_info_valid():
    vendor_name = "microsoft"
    product_name = "teams"
    response = client.get(f"/vendors/{vendor_name}/products/{product_name}")

    assert response.status_code == 200
    data = response.json()

    assert 'id' in data
    assert 'created_at' in data
    assert 'updated_at' in data
    assert 'name' in data

def test_get_product_info_invalid():
    vendor_name = "microsofttttttttttttt"
    product_name = "teams"
    response = client.get(f"/vendors/{vendor_name}/products/{product_name}")

    assert response.status_code == 404
    data = response.json()

    assert 'detail' in data

def test_get_product_info_invalid2():
    vendor_name = "microsoft"
    product_name = "teamssssssss"
    response = client.get(f"/vendors/{vendor_name}/products/{product_name}")

    assert response.status_code == 404
    data = response.json()

    assert 'detail' in data

def test_get_product_cve_valid():
    vendor_name = "microsoft"
    product_name = "teams"
    response = client.get(f"/vendors/{vendor_name}/products/{product_name}/cve")

    assert response.status_code == 200
    data = response.json()

    assert 'count' in data
    assert 'next' in data
    assert 'previous' in data
    assert 'results' in data

def test_get_product_cve_invalid():
    vendor_name = "microsofttttttttttttt"
    product_name = "teams"
    response = client.get(f"/vendors/{vendor_name}/products/{product_name}/cve")

    assert response.status_code == 404
    data = response.json()

    assert 'detail' in data

def test_get_product_cve_invalid2():
    vendor_name = "microsoft"
    product_name = "teamsssssss"
    response = client.get(f"/vendors/{vendor_name}/products/{product_name}/cve")

    assert response.status_code == 404
    data = response.json()

    assert 'detail' in data

def test_get_product_cve_valid_with_page():
    vendor_name = "microsoft"
    product_name = "teams"
    response = client.get(f"/vendors/{vendor_name}/products/{product_name}/cve?page=2")

    assert response.status_code == 200
    data = response.json()

    assert 'count' in data
    assert 'next' in data
    assert 'previous' in data
    assert 'results' in data



def test_get_product_cve_invalid_with_page():
    vendor_name = "microsoft"
    product_name = "teams"
    response = client.get(f"/vendors/{vendor_name}/products/{product_name}/cve?page=10000")

    assert response.status_code == 404
    data = response.json()

    assert 'detail' in data
