from flask import session, g
from flask_login import UserMixin
from app import login_manager
from app import get_db

def get_current_user():
    curr_user = None
    if 'user_id' in session:
        user_id = session['user_id']
        cur = get_db()
        cur.execute('select * from v_users where id=%s',(user_id,))
        curr_user = cur.fetchone()

    return curr_user


