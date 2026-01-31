from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
import time

from .database import engine, Base, get_db
from . import models, schemas, crud

app = FastAPI()

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # OK for now (prod later restrict)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- DB STARTUP (IMPORTANT) --------------------
@app.on_event("startup")
def startup_db():
    retries = 10
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database connected and tables created")
            break
        except OperationalError:
            print("⏳ Database not ready, retrying...")
            retries -= 1
            time.sleep(3)
    else:
        raise Exception("❌ Could not connect to database")

# -------------------- ROUTES --------------------

@app.get("/")
def root():
    return {"message": "Restaurant Booking API is running!"}

@app.post("/book", response_model=schemas.BookingResponse)
def book_table(
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db)
):
    return crud.create_booking(db, booking)

# Create table (admin)
@app.post("/admin/tables", response_model=schemas.TableResponse)
def add_table(
    table: schemas.TableCreate,
    db: Session = Depends(get_db)
):
    return crud.create_table(db, table)

# Get all bookings (admin)
@app.get("/admin/bookings", response_model=list[schemas.BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    return crud.get_all_bookings(db)

# Delete booking (admin)
@app.delete("/admin/bookings/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    result = crud.delete_booking(db, booking_id)
    if not result:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted successfully"}
