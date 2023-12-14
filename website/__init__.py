from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
DB_NAME = "trial.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yoecur'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = 'static/images'  # Set the upload folder for images
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Set max upload size to 16MB
    
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    

    from .models import User,Car,Booking,CarPrice
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    from .admin import CarPriceAdminView
    
    admin = Admin(app, name='Brill Car Rental Dashboard', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))#loads the User module to the admin view
    admin.add_view(ModelView(Car, db.session))#loads car module to the admin view
    admin.add_view(ModelView(Booking, db.session))
    admin.add_view(CarPriceAdminView(CarPrice, db.session))

    @login_manager.user_loader
    def load_user(id):
        """Define load_user.
        ARGS:
            id(int): creates unique id.
        Return:
            return app.
        """
        return User.query.get(int(id))

    return app

def create_db(app):
    """Define create_db that creates a database."""
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app= app)
        print("database created successfully")
