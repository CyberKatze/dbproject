from flask import render_template, flash
from .form import SignUpForm, LoginForm
from . import main

@main.route('/')
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


@main.route('/signup', methods=['GET', 'POST'])
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


@main.route('/post')
def post():
    return render_template('post.html', post=None)


@main.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('sign-in.html', form=form)

