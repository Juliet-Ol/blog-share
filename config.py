import os

basedir = os.path.abspath(os.path.dirname(__file__))

# from instance.config import RANDOM_QUOTES_URL

class Config ():

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or\
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')




class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+pysopg2://bwdjvsasrlaeen:18d1081283ae243f3f0cb43119c2906ffb29f01255dc6d19bfb89f414c70af73@ec2-44-194-167-63.compute-1.amazonaws.com:5432/ddq6aoibtd4ceh'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+pysopg2://juliet:juliet@localhost/quote'

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}    


    

