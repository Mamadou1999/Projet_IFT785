from user import User
from app import db


class Company(User):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(255))
    logo = db.Column(db.String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'company',
    }
