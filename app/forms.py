from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField
from datetime import datetime

class RecipeForm(FlaskForm): # form for creating recipe
    title = StringField('Title', validators=[validators.DataRequired()])
    description = TextAreaField('Description', validators=[validators.DataRequired()]) 
    ingredients = TextAreaField('Ingredients', validators=[validators.DataRequired()])
    instructions = TextAreaField('Instructions', validators=[validators.DataRequired()])
    submit =  SubmitField("Create Recipe")
    remember_me = BooleanField("Remember Me")

class RegistrationForm(FlaskForm): # form for user registration
    username = StringField('USERNAME', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])
    remember_me = BooleanField("Remember Me")
    submit =  SubmitField("Register")
