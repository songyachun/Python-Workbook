from datetime import datetime
# from flask import render_template,session,redirect,url_for,current_app
from flask import render_template
from . import main
# from .forms import NameForm
# from .. import db
# from ..models import User
# from ..email import send_email

# @main.route('/', methods=['GET', 'POST'])
@main.route('/')
def index():
    return render_template('index.html')
