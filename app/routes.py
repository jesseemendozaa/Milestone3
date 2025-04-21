from ctypes import resize
from app import myapp_obj
from flask import render_template
from flask import redirect
from flask import Flask, request # Added flask and request
from flask_sqlalchemy import SQLAlchemy # Added SQLAlchemy
from app.forms import RecipeForm, RegistrationForm # importing from forms.py
from app.models import Recipe, User # importing from models.py
from app import db
from datetime import datetime # added datetime
# from <X> import <Y>

'''
Setup instructions:

Clone repo
Navigate to folder

run: 
python3 -m venv venv
source venv/bin/activate

install necessary libraries using pip3

run in terminal:
flask shell
from app import db
db.create.all()
exit()

python3 run.py

run in terminal to stop virtual environment:

deactivate

'''

@myapp_obj.route("/") # http://127.0.0.1:5000/
def main():
    recipe = Recipe.query.all() # get all recipes
    return render_template("hello.html", recipe=recipe)

@myapp_obj.route("/recipe/new", methods=['GET', 'POST']) # http://127.0.0.1:5000/recipe/new
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        #create recipe
        new_recipe = Recipe(title=form.title.data, description=form.description.data, ingredients=form.ingredients.data, instructions=form.instructions.data, date=datetime.now())
        db.session.add(new_recipe) #adding to database
        db.session.commit()
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("new.html", form=form) #recipe form

@myapp_obj.route("/recipe/<int:integer>") # http://127.0.0.1:5000/recipe/<enter number here>
def return_recipe(integer):
    recipe = Recipe.query.get(integer) # get recipe number
    if recipe is None:
        print("Recipe not found") #prints to terminal
        return ""
    return render_template("return_rec.html", recipe=recipe)

@myapp_obj.route("/recipe/<int:integer>/delete") # http://127.0.0.1:5000/recipe/<enter number here>/delete
def delete_recipe(integer):
    del_rec = Recipe.query.get(integer) # get recipe number
    db.session.delete(del_rec) #delete
    db.session.commit()

    return f"Recipe deleted: {integer}"

@myapp_obj.route("/registration", methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data #1
        email = form.email.data
        password = form.password.data #1

        u = User(username=username, email=email, password=password) #1
        db.session.add(u)#1
        db.session.commit() #1
        
        print(f"User registered: {username}")
        return redirect("/")
    return render_template("registration.html", form=form)