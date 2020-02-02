from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class AuthorFomr(FlaskForm):
    author_usr = StringField('add author',validators=[InputRequired()])