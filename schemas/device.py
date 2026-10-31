from pydantic import BaseModel,Field
from typing import Any

class DeviceBase(BaseModel):
    statusCode: int
    error: str | None = None
    message: str
    data: Any | None=None

class DeviceCreate(BaseModel):
    device_code: str = Field(max_length=10,min_length=4)
    price: float = Field(gt=0)
    device_type_id: int

class DeviceRespone(DeviceCreate):
    id: int

    class Config:
        from_attributes = True