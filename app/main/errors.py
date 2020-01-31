from flask import render_template, g
from . import main

@main.teardown_app_request
def close_db(error):
    if hasattr(g, 'db'):
        g.db[0].close()


@main.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page not Found"), 404


@main.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', message="Page not Found"), 500