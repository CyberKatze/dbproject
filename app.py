from flask import Flask, render_template, request, redirect, url_for, g
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired
from database import get_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class MyForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db[0].close()


@app.route('/')
def index():
    conn, cur = get_db()
    cur.execute('select * from users')
    result = cur.fetchall()
    return render_template('index.html', users=result)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = MyForm()
    if form.validate_on_submit():
        conn, cur = get_db()
        cur.execute('insert into users(username,email,password) values(%s,%s,%s)',
                    (form.username.data, form.email.data, form.password.data))
        conn.commit()
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)
