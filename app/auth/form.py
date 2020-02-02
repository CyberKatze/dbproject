from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class SignUpForm(LoginForm):
    email = StringField('Email', validators=[InputRequired()])
    firstname = StringField('First Name', validators=[])
    lastname = StringField('Last Name', validators=[])
    

