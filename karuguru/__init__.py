from flask import Flask, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    def robots_txt():
        return send_from_directory(os.getcwd(), 'robots.txt')
      # Google site verification route
    @app.route('/google6c098f75def709f5.html')
    def google_verify():
        return send_from_directory(os.getcwd(), 'google6c098f75def709f5.html')
    
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
