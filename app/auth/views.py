from flask import render_template, g, flash
from . import auth
from .form import SignUpForm, LoginForm


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        try:
            cur = get_db()
            cur.execute('insert into users(username,email,password) values(%s,%s,%s)',
                        (form.username.data, form.email.data, form.password.data))
            g.postgres_db_conn.commit()
            return redirect(url_for('index'))
        except:
            flash("Couldn't conncect to database")

    return render_template('auth/signup.html', form=form)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/sign-in.html', form=form)