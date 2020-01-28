from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class MyForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    form = MyForm()
    if form.validate_on_submit():
        redirect(url_for('index'))

    return render_template('signup.html', form=form)
