from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Table, Text
from user import User

class Company(User):
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    company_name = Column(String(255), nullable=False)
    description = Column(Text)
    location = Column(String(255))
    logo = Column(String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'company',
    }
