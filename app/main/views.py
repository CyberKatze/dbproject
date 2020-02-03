from flask import render_template, g, redirect, url_for,request
from . import main
from .. import get_db
from ..model import get_current_user
from datetime import datetime


@main.route('/')
def index():
    curr_user = get_current_user()
    cur = get_db()
    cur.execute("select p.p_id as pid, p.subject as title, a.des as des from article as a join post as p on p.p_id=a.p_id")
    results = cur.fetchall()
    
    return render_template('index.html', user=curr_user, art_des=results)



@main.route('/post_article')
def post_article():
    pid= request.args.get('pid')
    user =get_current_user()
    cur = get_db()

    cur.execute('select subject, date, type from post where p_id=%s',(pid,))
    article = cur.fetchone()

    if article is None or article['type']=='article':
        return render_template('error.html',message='Page has not found')
    
    pretty_date = datetime.strftime(article['date'], '%d %B, %Y, %I:%M%p')

    cur.execute('select script, seq_num from text_content where p_id =%s',(pid,))
    contents = cur.fetchall()
    cur.execute('select a.username from _user as a join article_author as aa on a.id=aa.id where aa.p_id=%s',
                (pid,))
    authors = cur.fetchall()
    cur.execute('select tag from post_tag where p_id=%s', (pid,))
    tags = cur.fetchall()
    return render_template('post.html',user=user,t=article['subject'], authors=authors,date=pretty_date, contents=contents, tags=tags)



