from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, SelectField, FloatField, StringField, PasswordField
from wtforms.validators import DataRequired, Email

class BookingForm(FlaskForm):
    """
    Form for booking a car.
    """
    car_id = SelectField('Select Car', coerce=int, validators=[DataRequired()])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    confirm_booking = SubmitField('Confirm Booking')
    
    from .models import Car  
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # Populate the car_id choices with car ids and names
        self.car_id.choices = [(car.id, car.name) for car in Car.query.all()]

class CarPriceForm(FlaskForm):
    """
    Form for updating car prices.
    """
    base_price = FloatField('Base Price', validators=[DataRequired()])
    submit = SubmitField('Update Price')

class EditProfileForm(FlaskForm):
    """
    Form for editing user profile information.
    """
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('New Password')
    submit = SubmitField('Update Profile')

