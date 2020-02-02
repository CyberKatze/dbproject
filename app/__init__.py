from flask import Flask, render_template, request, redirect, url_for, g, flash
from database import get_db
from config import config
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.signin'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    # login_manager.init_app(app)
    return app    

