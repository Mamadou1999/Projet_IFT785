from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_jwt_extended import JWTManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    JWTManager(app)

    # Enregistrer les Blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    return app