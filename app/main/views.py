from flask import render_template, g 
from . import main
from .. import get_db
from ..model import get_current_user



@main.route('/')
def index():
    curr_user = get_current_user()
    
    return render_template('index.html', user=curr_user)



@main.route('/post')
def post():
    return render_template('post.html', post=None)



