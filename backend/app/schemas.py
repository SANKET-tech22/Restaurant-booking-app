from pydantic import BaseModel
from datetime import date, time

class BookingCreate(BaseModel):
    name: str
    phone: str
    date: date
    time: time
    guests: int

class BookingResponse(BookingCreate):
    id: int
    status: str

    class Config:
        from_attributes = True   # new pydantic v2 style


# Add Tables create schema  
class TableCreate(BaseModel):
    table_number: int
    capacity: int

class TableResponse(TableCreate):
    id: int

    class Config:
        from_attributes = True
