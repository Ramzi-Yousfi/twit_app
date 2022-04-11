from flask import Flask,render_template
import os
import config
from dotenv import load_dotenv 
from flask_login import LoginManager
from app.API import api
from app.models import db,ma,migrate


# Global variables
login_manager = LoginManager()

# create app
def create_app():
    app = Flask(__name__)

    # Load environment variables from .env file
    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)
    app.config.from_object('config.settings.' + os.environ.get('FLASK_ENV'))



    # Initialize the extentions (app factory)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

      #Dtaabase models 
    from app.models.users import User
    from app.models.posts import Post
        
    with app.app_context():
        #Dtaabase tables
        db.create_all()
        db.session.commit()
    
        #Small HTTP Errors Handling
        @app.errorhandler(404)
        def page_not_found(e):
            return render_template('errors/404.html'), 404
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        #Blueprints
        #Blueprint for the non-auth parts of the app
        from app.views.home import home as home_blueprint
        app.register_blueprint(home_blueprint)
        #Blueprint for the auth parts of the app
        from app.views.auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        return app