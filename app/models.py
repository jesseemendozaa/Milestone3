from app import db
from datetime import datetime
from . import login_manager
from flask_login import UserMixin

class Recipe(db.Model): #Recipe created by user
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80)) #max length 80 characters
    description = db.Column(db.Text) #text box
    ingredients = db.Column(db.Text) #text box
    instructions = db.Column(db.Text) #text box
    date = db.Column(db.DateTime)

class User(db.Model, UserMixin): #Account info
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique = True , nullable = False) #max length 32 characters
    email = db.Column(db.String(100), unique = True , nullable = False) #max length 100 characters
    password = db.Column(db.String(32), nullable = False) #max length 32 characters

@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

