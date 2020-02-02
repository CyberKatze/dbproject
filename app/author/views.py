from flask import render_template, g, flash, url_for, redirect, session,request
from . import author
from .. import get_db
from .form import AuthorFomr

@author.route('/add_article',methods=['GET','POST'])
def add_article():
    if request.method=='POST' and request.form.get('title') and request.form.get('article'):
        return request.form.get('article')
    return render_template('author/add_article.html')