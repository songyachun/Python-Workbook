from flask_sqlalchemy import SQLAlchemy
import os
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from datetime import datetime
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for, flash

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# print(app.config)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
moment = Moment(app)
# ----------------------定义模型------------------------------


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


# -------------------路由与视图函数-------------------------------

class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name! ')
        session['name'] = form.name.data
        # name = form.name.data
        # form.name.data = ''
        # return redirect(url_for('index'))
        return redirect('/')
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
