import sys
import os
from fastapi.testclient import TestClient
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

client = TestClient(app)
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

def is_sorted_by_criteria(cve_list, criteria):
    
    for i in range(len(cve_list) - 1):
        current = cve_list[i][criteria]
        next_item = cve_list[i + 1][criteria]

        if criteria == "criticality":
            if current is None:
                current = float('-inf')
            if next_item is None:
                next_item = float('-inf')

            if current < next_item:
                return False
        elif criteria == "name":
            if current.lower() > next_item.lower():
                return False
        else:
            current_date = datetime.strptime(cve_list[i]['date'], DATE_FORMAT)
            next_date = datetime.strptime(cve_list[i + 1]['date'], DATE_FORMAT)

            if current_date < next_date:
                return False

    return True

def test_check_if_results():

    response = client.get("/filtering/vendor/microsoft/product/windows/sorting/date/")
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)

def test_sort_by_criticality():
    response = client.get("/filtering/vendor/microsoft/product/windows/sorting/criticality")
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)
    assert is_sorted_by_criteria(json_response, "criticality")

def test_sort_by_date():
    response = client.get("/filtering/vendor/fortinet/product/fortianalyzer/sorting/date")
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)
    assert is_sorted_by_criteria(json_response, "date")

def test_sort_by_name():
    response = client.get("/filtering/vendor/microsoft/product/windows/sorting/name")
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)
    assert is_sorted_by_criteria(json_response, "name")

def test_invalid_sorting_option():
    response = client.get("/filtering/vendor/microsoft/product/windows/sorting/invalid")
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)
    assert is_sorted_by_criteria(json_response, "criticality")

def test_missing_vendor():
    response = client.get("/filtering/vendor/product//windows/sorting/date")
    assert response.status_code == 404

def test_missing_product():
    response = client.get("/filtering/vendor/microsoft/product//sorting/date")
    assert response.status_code == 404
