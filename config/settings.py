import os 
class Config:
    DEFAULT = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('ENV')
    FLASK_APP = os.environ.get('APP_NAME')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

class development(Config):
    DEBUG = True
    

class production(Config):
    DEBUG = False
    PORT = os.environ.get('PORT') or 8080
 