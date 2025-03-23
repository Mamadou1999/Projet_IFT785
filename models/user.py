from datetime import datetime
# from app.extensions import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Table


# Création de la base déclarative pour tous les modèles
Base = declarative_base()

class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())

    type = Column(String(50))  # Pour la classe héritée (Company ou Developer)
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

