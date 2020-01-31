from flask import Flask, render_template, request, redirect, url_for, g, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired
from database import get_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class SignUpForm(LoginForm):
    email = StringField('Email', validators=[InputRequired()])


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db[0].close()


@app.route('/')
def index():
    result = None
    try:
        conn = get_db()
        cur = conn[1]
        cur.execute('select * from users')
        result = cur.fetchall()
    except:
        pass
    return render_template('index.html', users=result)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        try:
            db = get_db()
            conn = db[0]
            cur = db[1]
            cur.execute('insert into users(username,email,password) values(%s,%s,%s)',
                        (form.username.data, form.email.data, form.password.data))
            conn.commit()
            return redirect(url_for('index'))
        except:
            flash("Couldn't conncect to database")

    return render_template('signup.html', form=form)


@app.route('/post')
def post():
    return render_template('post.html', post=None)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('sign-in.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page not Found"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', message="Page not Found"), 500
