from flask import render_template, flash, redirect, url_for, request,Blueprint
from app.forms.users import LoginForm , RegisterForm



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title ='connexion'
    form = LoginForm()
    if request.method == 'GET':
        return render_template('auth/login.html', form=form ,titre=title)
    '''
    else:
        flash('You have been logged in')
        return redirect(url_for('main.index'))
    '''

@auth.route('/register', methods=['GET', 'POST'])
def register():
    title ='inscription'
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('auth/register.html',form=form, titre=title)
    