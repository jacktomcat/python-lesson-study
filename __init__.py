# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify,json
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Blueprint
from config import config

#bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
main = Blueprint('main', __name__) 
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name]) 
    config[config_name].init_app(app)
    
    #bootstrap.init_app(app)
    #mail.init_app(app)
    #moment.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here
    return app