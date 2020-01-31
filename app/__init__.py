from flask import Flask, render_template, request, redirect, url_for, g, flash
from database import get_db
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app    

