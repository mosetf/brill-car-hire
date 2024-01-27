from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime, timedelta
import logging

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    id_number = db.Column(db.Integer, unique=True, nullable=False)
    na_me = db.Column(db.String(200))
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)#rlship with Booking module

class Car(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # New name column
    model = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(200),nullable=False)
    engine = db.Column(db.String(10), nullable=False)
    bookings = db.relationship('Booking', backref='car', lazy=True)#rlship with booking
    prices = db.relationship('CarPrice', backref='car', lazy=True)

class Booking(db.Model, UserMixin):
    """
    Represents a booking made by a user for a car.
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='booked')  # 'booked', 'active', 'completed'
    total_price = db.Column(db.Float, nullable=False, default=0.0)

    def time_remaining(self):
        """
        Calculates the remaining time for the booking.

        Returns:
            str: A string representation of the remaining time in the format "X days, X hours, X minutes, X seconds".
        """
        now = datetime.utcnow()
        remaining_time = max(self.end_date - now, timedelta(0))
        
        days = remaining_time.days
        seconds = remaining_time.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Log the calculated time components
        logging.info(f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

        time_components = []
        if days > 0:
            time_components.append(f"{days} {'day' if days == 1 else 'days'}")
        if hours > 0 or days > 0:
            time_components.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
        if minutes > 0 or days > 0 or hours > 0:
            time_components.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
        if seconds > 0 or days > 0 or hours > 0 or minutes > 0:
            time_components.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")

        # Log the final time remaining string
        time_remaining_str = ' '.join(time_components).strip()
        logging.info(f"Time Remaining: {time_remaining_str}")

        return time_remaining_str

    def calculate_fine(self):
        """
        Calculates the fine for the booking if it has ended.

        Returns:
            float: The fine amount in dollars.
        """
        now = datetime.utcnow()
        time_elapsed = now - self.end_date
        if time_elapsed > timedelta(0):  # Fine only applies if the booking has ended
            fine_per_day = 500
            return fine_per_day * (time_elapsed.days + 1)  # Add 1 to include the current day
        else:
            return 0

class CarPrice(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), unique=True, nullable=False)
    base_price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    

    def __repr__(self):
        return f"<CarPrice {self.id}>"            