# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://monuser:monmotdepasse@localhost/adoptdev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'maclesecrete'
    JWT_SECRET_KEY = 'maclé_pour_jwt'
