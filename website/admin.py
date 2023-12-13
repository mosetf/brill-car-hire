from flask_admin.contrib.sqla import ModelView
from .models import CarPrice
from flask_login import current_user

# Create a custom admin view for CarPrice model
class CarPriceAdminView(ModelView):
    # Specify the columns to be displayed in the list view
    column_list = ['car_id', 'base_price', 'category']

    # Define a method to check if the current user has access to this view
    def is_accessible(self):
        # Access is granted only if the user is authenticated and is an admin
        return current_user.is_authenticated and current_user.is_admin

