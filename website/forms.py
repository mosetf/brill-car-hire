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

