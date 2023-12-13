from flask import Blueprint, render_template,request,flash,redirect,url_for
from .models import User, Car
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import logout_user, login_user,login_required,current_user
from sqlalchemy import or_

auth = Blueprint('auth', __name__)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Define login."""
    if request.method == "POST":
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')

        # Query the user by email or phone
        user = User.query.filter(or_(User.email == email, User.phone == phone)).first()

        # Check if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            # Check if the user is an admin
            if user.is_admin:
                flash('Logged in successfully as admin', category='success')
            else:
                flash('Logged in successfully', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        elif user is None:
            flash('Email or phone number doesn\'t exist', category='error')
        else:
            flash('Incorrect password, try again!', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    """Define logout return a redirection to the website home page."""
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/admin-sign-up', methods=('GET', 'POST'))
def admin_sign_up():
    if request.method == 'POST':
        # ... collect form data ...
        new_admin = User(email=email, password=generate_password_hash(
            password, method='pbkdf2:sha256'), is_admin=True)
        db.session.add(new_admin)
        db.session.commit()
        flash('Admin account created!', category='success')
        return redirect(url_for('auth.login'))
    return render_template("admin_sign_up.html", user=current_user)

@auth.route('/sign-up', methods=('GET', 'POST'))
def sign_up():
    if request.method == 'POST':
        phone = request.form.get('Phone')
        email = request.form.get('email')
        id_number = request.form.get('id_number')
        na_me = request.form.get('Name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #user = User.query.filter_by(or_(phone==phone, email==email)).first()
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif phone is None or  len(str(phone).strip()) != 10:
            #rint(phone, type(phone), len(str(phone).strip()))
            flash('Phone number must be exactly 10 digits', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(id_number) < 4:
            flash('ID number must be 10 digits', category='error')
        elif len(na_me) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email,phone=phone,na_me=na_me,id_number=id_number, password=generate_password_hash(
                password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html", user=current_user)


from werkzeug.utils import secure_filename
import os


@auth.route('/add_car', methods=['GET', 'POST'])
@login_required
def add_car():
    if request.method == 'POST':
        name = request.form.get('name')
        model = request.form.get('model')
        description = request.form.get('description')
        car_image = request.files['car_image']
        engine = request.form.get('engine')

        # Check if any of the fields are empty
        if not name:
            flash('Name is required.', 'warning')
        if not model:
            flash('Model is required.', 'warning')
        if not description:
            flash('Description is required.', 'warning')
        if not car_image:
            flash('Car image is required.', 'warning')
        if not engine:
            flash('engine type is required', 'warning')

        # Only proceed if all fields are provided
        if  name and model and description and car_image:
            filename = secure_filename(car_image.filename)
            image_path = os.path.join('website/static/images', filename)
            car_image.save(image_path)

            new_car = Car( name=name,model=model, description=description, image_url=image_path, engine=engine)
            db.session.add(new_car)
            db.session.commit()

            return redirect(url_for('auth.add_car'))
    return render_template('car_form.html', user=current_user)
