from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

class JobForm(FlaskForm):
    title = StringField('Titre du Poste', validators=[DataRequired(), Length(max=150)])
    company_name = StringField('Nom de l’Entreprise', validators=[DataRequired(), Length(max=150)])
    location = StringField('Lieu', validators=[DataRequired(), Length(max=150)])
    description = TextAreaField('Description du Poste', validators=[DataRequired()])
    requirements = TextAreaField('Compétences Requises', validators=[Length(max=1000)])
    salary_range = StringField("Fourchette de salaire", validators=[Optional()])
