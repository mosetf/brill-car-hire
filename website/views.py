from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

# Import models and database from the current package
from .models import Booking, db

# Define a Blueprint for views
views = Blueprint('views', __name__)


# Define the route for the home page
@views.route('/', methods=['GET', 'POST'])
def home():
    import os

    image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
    images = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]

    if current_user.is_authenticated:
        from .models import Car

        cars = Car.query.all() 
        return render_template("home.html", user=current_user, cars=cars)
        
    return render_template('index.html', images=images) 

# Define the route for booking a car
@views.route('/book_car/<int:car_id>', methods=['GET', 'POST'])
@login_required  # Ensure the user is logged in
def book_car(car_id):
    # Import necessary modules and models from the current package
    from .booking import create_booking
    from .forms import BookingForm
    from .models import Car

    # Initialize the booking form
    form = BookingForm()
    form.car_id.choices = [(car.id, car.name) for car in Car.query.all()]

    # Validate the form submission
    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data

        # Create a new booking
        booking = create_booking(current_user.id, car_id, start_date, end_date)

        if booking:
            # Redirect to the payment selection page with the new booking's ID.
            return redirect(url_for('views.select_payment', booking_id=booking.id))
        else:
            return render_template('book_car.html', form=form, car_id=car_id)

    return render_template('book_car.html', form=form, car_id=car_id)

# Define the route for the user dashboard
@views.route('/dashboard')
@login_required  # Ensure the user is logged in
def dashboard():
    # Import Booking model from the current package
    from .models import Booking

    # Fetch all bookings for the current user, ordered by start date
    bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.start_date.desc()).all()
    return render_template('dashboard.html', bookings=bookings)

# Import Car and CarPrice models from the current package
from .models import Car, CarPrice

# Define a function to get the price of a car
def get_car_price(car_id):
    car_price = CarPrice.query.filter_by(car_id=car_id).first()
    return car_price.base_price if car_price else None

# Define the route for viewing a car
@views.route('/car/<int:car_id>')
def view_car(car_id):
    # Fetch the car record from the database
    car = Car.query.get_or_404(car_id)
    car_price = get_car_price(car_id)
    return render_template('car_detail.html', car=car, car_price=car_price)

# Define the route for selecting a payment method
@views.route('/select_payment/<int:booking_id>', methods=['GET', 'POST'])
@login_required  # Ensure the user is logged in
def select_payment(booking_id):
    # Fetch the booking record from the database
    booking = Booking.query.get_or_404(booking_id)

    if request.method == 'POST':
        payment_method = request.form.get('payment_method')

        # Process the payment
        if process_payment(booking_id, payment_method):
            booking.status = 'confirmed'  # Update the booking status to confirmed
            db.session.commit()
            flash('Payment successful and booking confirmed!', 'success')
            return redirect(url_for('views.dashboard'))
        else:
            flash('Payment failed. Please try again.', 'error')

    return render_template('payment_selection.html', booking=booking)

# Define a function to process a payment
def process_payment(booking_id, payment_method):
    # Mock payment processing logic
    # In a real scenario, you would integrate with a payment gateway API here
    # For demonstration purposes, we'll assume the payment is always successful
    print(f"Processing payment for booking ID {booking_id} using {payment_method}")
    return True  # Return True to simulate a successful payment

# Define the route for editing a user profile
@views.route('/edit_profile', methods=['GET', 'POST'])
@login_required  # Ensure the user is logged in
def edit_profile():
    # Import the form for editing a profile from the current package
    from .forms import EditProfileForm

    # Initialize the form
    form = EditProfileForm()

    # Validate the form submission
    if form.validate_on_submit():
        # Update user information in the database
        current_user.name = form.name.data
        current_user.email = form.email.data
        if form.password.data:
            pass
           # current_user.set_password(form.password.data)

        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('views.dashboard'))

    # Pre-fill the form with current user information
    form.name.data = current_user.na_me
    form.email.data = current_user.email

    return render_template('edit_profile.html', form=form)

