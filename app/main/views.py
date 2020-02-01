from flask import render_template
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



@main.route('/post')
def post():
    return render_template('post.html', post=None)



