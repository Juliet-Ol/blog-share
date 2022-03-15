from ensurepip import bootstrap
from flask import Flask
from config import Config, DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



# Initializing application

app = Flask(__name__,instance_relative_config = True)

# Setting up configuration from app import db
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)
db = SQLAlchemy()

db.init_app(app)

from app import views