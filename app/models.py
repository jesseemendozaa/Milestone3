from app import db
from datetime import datetime

class Recipe(db.Model): #Recipe created by user
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80)) #max length 80 characters
    description = db.Column(db.Text) #text box
    ingredients = db.Column(db.Text) #text box
    instructions = db.Column(db.Text) #text box
    date = db.Column(db.DateTime)

class User(db.Model): #Account info
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique = True , nullable = False) #max length 32 characters
    email = db.Column(db.String(100), unique = True , nullable = False) #max length 100 characters
    password = db.Column(db.String(32), nullable = False) #max length 32 characters
