from flask import render_template, flash, redirect, url_for, request,Blueprint



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')