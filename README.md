# CVE Checker

## Description

Small Application that allow user to check the CVE linked to a product or Software.

## Tools/API used

- OpenCVE
- Nginx
- FastAPI
- Docker

## How to use the application locally ?

1. Open the docker-compose.yml
2. Add environnement variable in "services:fastapi" just after "image" :

```
    image: cloudaccessnetwork/cve:fastapi-${TAG}
    environment:
      - USERNAME=your_username
      - PASSWORD=your_password
    container_name: fastapi_app
```