from fastapi import FastAPI
import uvicorn

from cves import router as cves_router
from products import router as products_router

app = FastAPI()

app.include_router(cves_router)
app.include_router(products_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
