from user import User
from app import db


class Developer(User):

    __tablename__ = 'developers'
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    programming_languages = db.Column(db.ARRAY(db.String))
    experience_levels = db.Column(db.ARRAY(db.Integer))
    minimum_salary = db.Column(db.Integer)
    biography = db.Column(db.Text)
    avatar = db.Column(db.String(255))
    location = db.Column(db.String(255))
    is_profile_public = db.Column(db.Boolean, default=True)

    __mapper_args__ = {
        'polymorphic_identity': 'developer',
    }
