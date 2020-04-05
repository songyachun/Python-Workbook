from flask import render_template, redirect, request, url_for, flash
from . import auth
from flask_login import login_user,login_required,logout_user
from .forms import LoginForm
from ..models import User
import pysnooper

@auth.route('/login', methods=['GET', 'POST'])
@pysnooper.snoop()
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/secret')
def secret():
    return 'Only authenticated users are allowed!'

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
