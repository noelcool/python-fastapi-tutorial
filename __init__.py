from fastapi import FastAPI
from request_body import ItemReq, ItemRes

import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def read_root(item: ItemReq): # request body
    return item


@app.post("/items/", response_model=ItemRes)
async def create_item(item: ItemReq):
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

