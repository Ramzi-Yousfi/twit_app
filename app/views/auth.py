
from webbrowser import get
from flask import render_template, flash, redirect, url_for, request,Blueprint,session
from app.forms.users import LoginForm , RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.users import User
from app import db 
from flask_login import login_user, logout_user, login_required,current_user

from threading import Timer


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title ='connexion'
    form = LoginForm()
    if request.method == 'GET':
        return render_template('auth/login.html', form=form ,titre=title)
    
    email = request.form.get('email')
    password = request.form.get('password')
    connect = ''
    user = User.query.filter_by(email=email).first()

    if user is None or  check_password_hash(user.password, password) == False:
        connect = 'no'
        flash('Email ou mot de passe incorrect')
        return render_template('auth/login.html', form=form ,titre=title ,connect=connect)
    login_user(user)
    session['username'] = current_user.username
    return redirect(url_for('home.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    title ='inscription'
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('auth/register.html',form=form, titre=title)
    
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    print(password)
    user = User.query.filter_by(email=email).first()
    red = ''
    if user:
        flash('Cet email est déjà utilisé')
        red = 'login'
        return render_template('auth/register.html', form=form, titre=title,red=red)
    if form.validate_on_submit():
        new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Vous êtes inscrit')
        return redirect(url_for('auth.login'))
    else:
        flash('Veuillez vérifier vos informations')
        return render_template('auth/register.html', form=form, titre=title)

@auth.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    logout_user()
    return redirect(url_for('home.index'))