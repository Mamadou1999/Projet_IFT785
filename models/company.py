from app.models.user import User
from app.extensions import db


class Company(User):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(255))
    logo = db.Column(db.String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'company',
    }
