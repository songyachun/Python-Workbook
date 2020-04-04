from flask import render_template
from . import auth
from flask_login import login_required

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/secret')
def secret():
    return 'Only authenticated users are allowed!'