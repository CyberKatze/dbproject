from flask import render_template, g, flash, url_for, redirect
from . import auth
from .form import SignUpForm, LoginForm
from .. import get_db
from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        
        cur = get_db()
        cur.execute('select username from _user where username=%s', (form.username.data,))
        if cur.fetchone() is None:
            pass_hash = generate_password_hash(form.password.data)
            cur.execute('insert into _user(username) values(%s)',
                        (form.username.data,))
            cur.execute("SELECT currval(pg_get_serial_sequence('_user','id'))")
            r =cur.fetchone()
            cur.execute('insert into ruser(id,pass,email,fname,lname) values(%s,%s,%s,%s,%s)',
                        (r[0], pass_hash, form.email.data,form.firstname.data,form.lastname.data ))
            g.postgres_db_conn.commit()
            cur.execute('select fname,id from ruser where id=%s', (r[0],))
            result= cur.fetchone()
            return "name: {}, id:{}".format(result['fname'], result['id'])
        else:
            flash("User already is registered")
    

    return render_template('auth/signup.html', form=form)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        cur = get_db()
        cur.execute('select id, username, pass from v_users where username=%s', (form.username.data,))
        user = cur.fetchone()
        if check_password_hash(user['pass'],form.password.data):
            return " Hello {} your have logined".format(user['username'])
    return render_template('auth/sign-in.html', form=form)