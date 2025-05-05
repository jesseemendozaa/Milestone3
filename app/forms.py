from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange
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

class LoginForm(FlaskForm):
    username = StringField('USERNAME', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    submit =  SubmitField("Login")

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[validators.DataRequired()])
    submit =  SubmitField("Submit Comment")


class RatingForm(FlaskForm):
    score = IntegerField('Rate (1-5)', validators=[validators.DataRequired(), NumberRange(min=1, max=5)])
    submit = SubmitField("Submit Rating")