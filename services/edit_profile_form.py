from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Optional, Length, NumberRange

class UpdateProfileForm(FlaskForm):
    name = StringField('Nom Complet', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    programming_languages  = StringField('Compétences', validators=[Optional(), Length(max=255)])
    minimum_salary = DecimalField('Salaire minimum', places=2, validators=[Optional(), NumberRange(min=0)])
    biography = TextAreaField('Biographie', validators=[Optional(), Length(max=1000)])
    location = StringField('Adresse', validators=[Optional(), Length(max=255)])
    experience_levels = IntegerField("Années d'expérience", validators=[Optional(), NumberRange(min=0)])
