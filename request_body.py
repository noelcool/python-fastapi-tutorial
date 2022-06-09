from pydantic import BaseModel
from typing import Union


class ItemReq(BaseModel):
    reason: str
    status: int
    description: Union[str, None] = None


class ItemRes(BaseModel):
    reason: str
    status: int
