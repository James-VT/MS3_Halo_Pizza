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


# The below route function is for our registration page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Here we check if the username exists already in db
        # Everything in db stored in lower case, hence lower() method.
        # existing_user will come back with a truthy value if
        # it finds a username that matches the one entered
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

# Checks if existing_user is truthy, which it will be if the
# username already exists. Then, if it does, it will redirect
# the user back to the register page to try again -
# basically just resetting the page.

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

# The below gathers the data entered into the form by the user,
# and stores it in the "register" variable as a dictionary.
# This acts as an "else" for the "if" above.

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(
                request.form.get("password"))
            }
        # The below goes into the users collection
        # within MongoDB and, since we declared the
        # register variable with the user's input made into
        # a dictionary above, all we need to is drop that
        # variable into it with the insert_one() method.
        mongo.db.users.insert_one(register)

        # Puts our new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Congratulations, you have successfully created your account!")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # This checks whether the username is in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # This ensures hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back, {}".format(
                        request.form.get("username")))
            else:
                # This is for an invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # This is for a username not existing
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))
            
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
