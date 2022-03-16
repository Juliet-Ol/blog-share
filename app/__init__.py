from flask import Flask
from importlib_metadata import requires
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


bootstrap = Bootstrap()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()



#initializing application

# def create_app(config_name):
app = Flask(__name__)
app.config.from_object(config_options['development'])

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"

bootstrap.init_app(app)
login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app)

from app import views


# @app.route('/')
# def index():
#     return 'OK';
