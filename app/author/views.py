from flask import render_template, g, flash, url_for, redirect, session,request
from . import author
from .. import get_db
from .form import AuthorFomr
from ..model import get_current_user

@author.route('/add_article',methods=['GET','POST'])
def add_article():
    user = get_current_user()
    if user is None or user['author']=='':
        return render_template('error.html',message='You are not allowed to access this page')
    if request.method=='POST' and request.form.get('title') and request.form.get('article'):
        cur = get_db()
        cur.execute('select post.p_id as p_id, post.type as type from post where subject=%s', (request.form['title'],))
        post = cur.fetchone()
        seq_num = 1
        if post:
            
            if post['type'].strip() == 'article':
                cur.execute('select max(seq_num) from post as p join content as c on c.p_id=p.p_id group by c.p_id')
                seq_num = cur.fetchone()[0] +1
                pid=post['p_id']
            else:
                flash('Title is already exist')
                return render_template('author/add_article.html')
        else:
            cur.execute('insert into post(subject, date, type) values(%s, NOW(), %s)', (request.form['title'].lower(),'article'))
            cur.execute("SELECT currval(pg_get_serial_sequence('post','p_id'))")
            pid = cur.fetchone()[0]
            cur.execute('insert into article(p_id) values(%s)',(pid,) )
            

        cur.execute('insert into article_author(p_id, id) values(%s, %s)',(pid,session['user_id']))
        for t in request.form['tags'].split('#'):
            if t != '':
                cur.execute('insert into post_tag(p_id, tag) values(%s,%s) on conflict do nothing' , (pid,t.lower().strip()))
        cur.execute('insert into content(p_id,seq_num) values(%s, %s)',(pid,seq_num))
        cur.execute('insert into text(p_id, seq_num) values(%s, %s)',(pid,seq_num))
        cur.execute('insert into text_content(p_id, seq_num,script,language) values(%s,%s,%s,%s)',
                        (pid, seq_num, request.form['article'],'en'))
        g.postgres_db_conn.commit()

        return request.form.get('article')+'author_id:{},post_id:{}'.format(session['user_id'],pid)
    return render_template('author/add_article.html',user=user)