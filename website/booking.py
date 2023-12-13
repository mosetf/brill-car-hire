from datetime import datetime
from .models import Car, Booking, CarPrice
from flask import flash
from . import db

def check_availability(car_id, start_date, end_date):
    """
    Check if a car is available for booking during the specified time frame.

    :param car_id: ID of the car to check availability for
    :param start_date: Start date of the desired booking
    :param end_date: End date of the desired booking
    :return: True if the car is available, False otherwise
    """
    # Ensure start_date and end_date are datetime.date objects
    if isinstance(start_date, datetime):
        start_date = start_date.date()
    if isinstance(end_date, datetime):
        end_date = end_date.date()

    # Query existing bookings for the specified car
    existing_bookings = Booking.query.filter_by(car_id=car_id).all()

    # Check for overlapping bookings
    for booking in existing_bookings:
        # Convert booking.start_date and booking.end_date to datetime.date if they are datetime.datetime
        booking_start_date = booking.start_date.date() if isinstance(booking.start_date, datetime) else booking.start_date
        booking_end_date = booking.end_date.date() if isinstance(booking.end_date, datetime) else booking.end_date

        if not (end_date < booking_start_date or start_date > booking_end_date):
            # There is an overlap, the car is not available
            return False

    # If no overlap, the car is available
    return True


def create_booking(user_id, car_id, start_date, end_date):
    """
    Create a new booking for a user and a car within a specified time frame.

    :param user_id: ID of the user making the booking
    :param car_id: ID of the car to be booked
    :param start_date: Start date of the booking
    :param end_date: End date of the booking
    :return: The created Booking object if successful, False otherwise
    """
    if check_availability(car_id, start_date, end_date):
        # Calculate the total price
        car_price = CarPrice.query.filter_by(car_id=car_id).first()
        if car_price:
            duration = (end_date - start_date).days + 1  # Add 1 to include the last day
            total_price = car_price.base_price * duration
        else:
            total_price = 0  # Default price if not found

        # Create a new Booking object
        new_booking = Booking(
            user_id=user_id,
            car_id=car_id,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price  # Set the total price
        )

        # Add the new booking to the database and commit changes
        db.session.add(new_booking)
        db.session.commit()

        flash('Booking successful!', 'success')
        return new_booking
    else:
        # Display an error message if the car is not available for the selected dates
        flash('This car is not available for the selected dates.\nFailed to create a booking. Please try again.', 'error')
        return False

