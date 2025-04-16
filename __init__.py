from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from app.models.user import User
from app.extensions import db

#db = SQLAlchemy()



login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    JWTManager(app)

    # Enregistrer les Blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # redirection automatique si non connecté
    

    return app