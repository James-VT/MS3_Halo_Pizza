import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# The below line of code creates a new instance of Flask,
# which is to be our app. So we store it in a variable
# named app.
app = Flask(__name__)

# The below code is where we pull our environment variables from our
# env.py file and assign them to variables here so that they can be
# used in our project.
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# The app argument below is the Flask app object declared above
# It makes sure that our app is properly using the Mongo database
mongo = PyMongo(app)


# The below route function gets us landing on our homepage by default
# and allows that page to access the recipes in our database.
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("home.html", recipes=recipes)


# The below route function  is for our registration page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Here we check if the username exists already in db
        # Everything in db stored in lower case, hence lower() method.
        # existing_user will come back with a truthy value if
        # it finds a username that matches the one entered

        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

# Checks if existing_user is truthy, which it will be if the
# username already exists. Then, if it does, it will redirect
# the user back to the register page to try again -
# basically just resetting the page

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))



            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_has(request.form.get("password"))
            }

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
