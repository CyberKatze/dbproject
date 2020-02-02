from flask import render_template, g, flash, url_for, redirect, session
from . import admin
from .. import get_db
from .form import AdminForm


@admin.route('/authors', methods=['GET','POST'])
def authors():
    form = AdminForm()
    cur = get_db()
    if form.validate_on_submit():
        cur.execute('select username,id from _user where username=%s',
                    (form.author_usr.data,))
        user = cur.fetchone()
        if user:
            cur.execute('insert into author(id) values(%s)', (user['id'],))
            g.postgres_db_conn.commit()
            return redirect(url_for('admin.authors'))
        else:
            flash("user doesn't exist")
    cur.execute('select author.id,username from _user join author on _user.id=author.id')
    authors_result = cur.fetchall()
    return render_template('admin/authors.html', authors=authors_result, form=form)

@admin.route('/author_del/<int:id>')
def author_del(id):
    cur = get_db()
    cur.execute('delete from author where id=%s',(id,))
    g.postgres_db_conn.commit()
    return redirect(url_for('admin.authors'))