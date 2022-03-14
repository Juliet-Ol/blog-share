from ensurepip import bootstrap
from flask import Flask
from config import Config, DevConfig
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration from app import db
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

from app import views