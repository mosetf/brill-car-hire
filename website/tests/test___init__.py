import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from .models import User, Car, Booking, CarPrice
from .admin import CarPriceAdminView
from . import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)
        self.login_manager = LoginManager()
        self.login_manager.login_view = 'auth.login'
        self.login_manager.init_app(self.app)
        self.admin = Admin(self.app, name='Brill Car Rental Dashboard', template_mode='bootstrap3')

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_create_app(self):
        self.assertIsInstance(self.app, Flask)
        self.assertEqual(self.app.config['SECRET_KEY'], 'yoecur')
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], f'sqlite:///{DB_NAME}')
        self.assertEqual(self.app.config['UPLOAD_FOLDER'], 'static/images')
        self.assertEqual(self.app.config['MAX_CONTENT_LENGTH'], 16 * 1024 * 1024)

    def test_create_app_db(self):
        with self.app.app_context():
            self.db.create_all()
            self.assertIsNotNone(User.query.first())
            self.assertIsNotNone(Car.query.first())
            self.assertIsNotNone(Booking.query.first())
            self.assertIsNotNone(CarPrice.query.first())

    def test_create_app_login_manager(self):
        self.assertEqual(self.login_manager.login_view, 'auth.login')
        self.assertEqual(self.login_manager.app, self.app)

    def test_create_app_admin(self):
        self.assertEqual(self.admin.name, 'Brill Car Rental Dashboard')
        self.assertEqual(self.admin.template_mode, 'bootstrap3')
        self.assertIsNotNone(self.admin.index_view)
        self.assertIsNotNone(self.admin._views)

if __name__ == '__main__':
    unittest.main()