from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('mot de passe', validators=[DataRequired(),Length(min=3)])
    confirm_password = PasswordField('confirmer mot de passe ',validators=[ DataRequired() ,EqualTo("password", message='Les mots de passe doivent être identiques')])
    submit = SubmitField('Inscription')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Mot De Passe', validators=[DataRequired()])
    submit = SubmitField('Log In')