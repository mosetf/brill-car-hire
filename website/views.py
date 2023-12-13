from flask import Blueprint, render_template, redirect, url_for,flash,redirect,request
from flask_login import login_required, current_user

from .models import Booking, db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    from .models import Car

    cars = Car.query.all() # Fetch all car records from the database
    return render_template("home.html", user=current_user, cars=cars)

@views.route('/book_car/<int:car_id>', methods=['GET', 'POST'])
@login_required
def book_car(car_id):
    from .booking import create_booking
    from .forms import BookingForm
    from .models import Car

    form = BookingForm()
    form.car_id.choices = [(car.id, car.model) for car in Car.query.all()]

    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data

        booking = create_booking(current_user.id, car_id, start_date, end_date)

        if booking:
            # Redirect to the payment selection page with the new booking's ID.
            return redirect(url_for('views.select_payment', booking_id=booking.id))
        else:
            return render_template('book_car.html', form=form, car_id=car_id)

    return render_template('book_car.html', form=form, car_id=car_id)


@views.route('/dashboard')
@login_required
def dashboard():
    from .models import Booking
    bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.start_date.desc()).all()
    return render_template('dashboard.html', bookings=bookings)



from .models import Car, CarPrice

def get_car_price(car_id):
    car_price = CarPrice.query.filter_by(car_id=car_id).first()
    return car_price.base_price if car_price else None

#not in work junk
@views.route('/car/<int:car_id>')
def view_car(car_id):
    car = Car.query.get_or_404(car_id)
    car_price = get_car_price(car_id)
    return render_template('car_detail.html', car=car, car_price=car_price)

@views.route('/select_payment/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def select_payment(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if request.method == 'POST':
        payment_method = request.form.get('payment_method')
        if process_payment(booking_id, payment_method):
            booking.status = 'confirmed'  # Update the booking status to confirmed
            db.session.commit()
            flash('Payment successful and booking confirmed!', 'success')
            return redirect(url_for('views.dashboard'))
        else:
            flash('Payment failed. Please try again.', 'error')
    return render_template('payment_selection.html', booking=booking)

def process_payment(booking_id, payment_method):
    # Mock payment processing logic
    # In a real scenario, you would integrate with a payment gateway API here
    # For demonstration purposes, we'll assume the payment is always successful
    print(f"Processing payment for booking ID {booking_id} using {payment_method}")
    return True  # Return True to simulate a successful payment

@views.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    from .forms import EditProfileForm
    form = EditProfileForm()

    if form.validate_on_submit():
        # Update user information in the database
        current_user.name = form.name.data
        current_user.email = form.email.data
        if form.password.data:
            current_user.set_password(form.password.data)

        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('views.dashboard'))

    # Pre-fill the form with current user information
    form.name.data = current_user.na_me
    form.email.data = current_user.email

    return render_template('edit_profile.html', form=form)    