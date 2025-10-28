# import os
# from typing import Dict

import os
from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def read_root(name: str):
    return {"message": f"Hello, {name}"}


@app.get("/items")
def get_items():
    items_list = [
        "item1",
        "item2",
    ]

    return {
        "items": items_list
    }
