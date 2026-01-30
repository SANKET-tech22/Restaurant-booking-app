from sqlalchemy.orm import Session
from . import models, schemas

def create_booking(db: Session, booking: schemas.BookingCreate):
    new_booking = models.Booking(
        name=booking.name,
        phone=booking.phone,
        date=booking.date,
        time=booking.time,
        guests=booking.guests,
        status="pending"
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking



# Create Table
def create_table(db: Session, table: schemas.TableCreate):
    new_table = models.Table(
        table_number=table.table_number,
        capacity=table.capacity
    )
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table


# API to view all bookings
def get_all_bookings(db: Session):
    return db.query(models.Booking).all()


# Delete Function
def delete_booking(db: Session, booking_id: int):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if booking:
        db.delete(booking)
        db.commit()
        return True
    return False