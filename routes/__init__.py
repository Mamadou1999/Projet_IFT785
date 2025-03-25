from app.controllers.auth_controller import auth_bp
from app.controllers.profile_controller import profile_bp
from app.controllers.job_controller import job_bp
from app.controllers.match_controller import match_bp
from app.controllers.search_controller import search_bp
from app.controllers.rating_controller import rating_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(profile_bp, url_prefix='/profile')
    app.register_blueprint(job_bp, url_prefix='/jobs')
    app.register_blueprint(match_bp, url_prefix='/match')
    app.register_blueprint(search_bp, url_prefix='/search')
    app.register_blueprint(rating_bp, url_prefix='/rating')
