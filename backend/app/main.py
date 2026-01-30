from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from . import models, schemas, crud

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Restaurant Booking API is running!"}

@app.post("/book", response_model=schemas.BookingResponse)
def book_table(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db, booking)

# Api endpoint to table creation
@app.post("/admin/tables", response_model=schemas.TableResponse)
def add_table(table: schemas.TableCreate, db: Session = Depends(get_db)):
    return crud.create_table(db, table)

# Get all bookings
@app.get("/admin/bookings", response_model=list[schemas.BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    return crud.get_all_bookings(db)

# Delete Route
@app.delete("/admin/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    result = crud.delete_booking(db, booking_id)
    if not result:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted successfully"}