from flask import Blueprint, render_template, redirect, make_response, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.users import User, Role
from extensions import db
from flask_login import login_user, login_required, logout_user
from common_functions import salt

user_bp = Blueprint("user",__name__, template_folder='templates')

@user_bp.route("/login")
def login_page():
    return render_template('login_page.html')

@user_bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    print(email)
    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, salt(password)):
        print("wrong")
        flash('Please check your login details and try again.')
        return redirect(url_for('user.login_page')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.home_page'))

@user_bp.route("/signup")
def signup_page():
    return render_template('signin_page.html')

@user_bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    login = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first() 

    if user: 
        flash('Email address already exists')
        return redirect(url_for('user.signup'))
    
    password =  generate_password_hash(salt(password), method='pbkdf2:sha256')
    new_user = User(email=email, login=login, password=password)
    role = Role.query.filter_by(slug="user").first()
    new_user.roles.append(role)
    db.session.add(new_user)
    db.session.commit()
    login_user(user, remember=False)
    return redirect(url_for('user.profile_page'))

@user_bp.route("/logout")
@login_required
def logout_page():
    logout_user()
    return redirect(url_for('main.home_page'))

@user_bp.route("/profil")
@login_required
def profil():
    return render_template("home.html")