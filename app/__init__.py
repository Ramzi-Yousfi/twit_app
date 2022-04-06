from flask import Flask,render_template
import os
import config
from dotenv import load_dotenv 



app = Flask(__name__)

# Load environment variables from .env file

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
app.config.from_object('config.settings.' + os.environ.get('ENV'))

#Dtaabase
from app.models import db,users
db.create_all()
db.session.commit()


#Small HTTP Errors Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


#Blueprints
#Blueprint for the non-auth parts of the app
from app.views.home import home as home_blueprint
app.register_blueprint(home_blueprint)
#Blueprint for the auth parts of the app
from app.views.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)