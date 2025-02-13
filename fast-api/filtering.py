import requests
from requests.auth import HTTPBasicAuth
import os
from fastapi import APIRouter, HTTPException

BASE_API_URL = "https://app.opencve.io/api/cve"
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

router = APIRouter()

def sorted_wrapper(list, value, reverse, has_null):

    if not reverse:
        return sorted(list, key=lambda x: x[value])
    if not has_null:
        return sorted(list, key=lambda x: x[value], reverse=True)
    return sorted(list, key=lambda x: x[value] if x[value] is not None else float('-inf'), reverse=True)


def construct_result_list(all_cve):

    output_list = {"list": []}

    for cve in all_cve:

        cve_response = requests.get(BASE_API_URL + "/" + cve["cve_id"] , auth=HTTPBasicAuth(USERNAME, PASSWORD))

        if cve_response.status_code != 200:
            raise HTTPException(status_code=cve_response.status_code, detail=cve_response.json())
        
        cve_json_response = cve_response.json()
        obj = {
            "name": cve_json_response["cve_id"],
            "title": cve_json_response["title"],
            "criticality": (cve_json_response["metrics"]["cvssV3_1"]["data"]).get("score", None),
            "date": cve_json_response["created_at"],
            "description": cve_json_response["description"]
        }

        output_list["list"].append(obj)

    return  output_list

@router.get("/filtering/vendor/{vendor_name}/")
def response(vendor_name: str):
    return {"Vendor": f"{vendor_name}"}


@router.get("/filtering/vendor/{vendor_name}/product/{product_name}/sorting/{sorting_type}/")
def filtering(vendor_name: str, product_name: str, sorting_type: str):

    
    response = requests.get(BASE_API_URL + "?vendor" + vendor_name + "&product=" + product_name , auth=HTTPBasicAuth(USERNAME, PASSWORD))

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    output_list = construct_result_list((response.json())["results"])

    match sorting_type:
        
        case "criticality":
            return sorted_wrapper(output_list["list"], "criticality", True, True)
        case "date":
            return sorted_wrapper(output_list["list"], "date", True, False)
        case "name" :
            return sorted_wrapper(output_list["list"], "name", False, False)
        case _:
            return sorted_wrapper(output_list["list"], "criticality", True, True)

