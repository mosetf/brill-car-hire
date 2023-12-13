from flask_admin.contrib.sqla import ModelView
from .models import CarPrice
from flask_login import current_user

class CarPriceAdminView(ModelView):
    column_list = ['car_id', 'base_price', 'category']

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin