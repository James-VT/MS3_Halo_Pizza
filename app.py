import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_paginate import Pagination, get_page_args
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
# To understand pagination, I consulted this:
# https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    # The list of recipes coming from mongodb is not
    # a true list, simply a Mongo Cursor Object. If
    # we wrap the entire find method in a Python list()
    # we turn it into a proper list.
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 4
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find().count()
    recipes = mongo.db.recipes.find()
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    # recipes = list(mongo.db.recipes.find())
    return render_template("home.html", recipes=recipes_paginated,
                            page=page,
                            per_page=per_page,
                            pagination=pagination)


@app.route("/view_by_category/<category_id>")
def view_by_category(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    recipes = mongo.db.recipes.find(
        {"category_name": category["category_name"]})

    return render_template("view_by_category.html", recipes=recipes, category=category)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
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
        return redirect(url_for("account", username=session["user"]))
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
                    return redirect(url_for(
                        "account", username=session["user"]))
            else:
                # This is for an invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # This is for a username not existing
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # grab the session user's username from db
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 4
    offset = (page - 1) * per_page
    total = mongo.db.recipes.find().count()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find({"created_by": username}))
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')

    return render_template("account.html", username=username,
                            recipes=recipes_paginated,
                            page=page,
                            per_page=per_page,
                            pagination=pagination)


@app.route("/logout")
def logout():
    flash("You have logged out. See you soon!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        is_vegetarian = True if request.form.get(
            "is_vegetarian") else False
        is_vegan = True if request.form.get(
            "is_vegan") else False
        is_gluten_free = True if request.form.get(
            "is_gluten_free") else False
        is_dairy_free = True if request.form.get(
            "is_dairy_free") else False
        recipe = {
            "pizza_name": request.form.get("pizza_name"),
            "image_url": request.form.get("image_url"),
            "short_description": request.form.get("short_description"),
            "category_name": request.form.getlist("category_name"),
            "ingredients": request.form.getlist("ingredients"),
            "cooking_steps": request.form.getlist("cooking_steps"),
            "is_vegetarian": is_vegetarian,
            "is_vegan": is_vegan,
            "is_gluten_free": is_gluten_free,
            "is_dairy_free": is_dairy_free,
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Thank you for submitting your recipe!")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# Below code pieced together from Code Institute's Task Manager's
# edit section. To show the pages, we only need to get the info
# through to the page by ID - everything else from the edit
# section was unnecessary.
@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_vegetarian = True if request.form.get(
            "is_vegetarian") else False
        is_vegan = True if request.form.get(
            "is_vegan") else False
        is_gluten_free = True if request.form.get(
            "is_gluten_free") else False
        is_dairy_free = True if request.form.get(
            "is_dairy_free") else False
        submit = {
            "pizza_name": request.form.get("pizza_name"),
            "image_url": request.form.get("image_url"),
            "short_description": request.form.get("short_description"),
            "category_name": request.form.getlist("category_name"),
            "ingredients": request.form.getlist("ingredients"),
            "cooking_steps": request.form.getlist("cooking_steps"),
            "is_vegetarian": is_vegetarian,
            "is_vegan": is_vegan,
            "is_gluten_free": is_gluten_free,
            "is_dairy_free": is_dairy_free
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe successfully updated!")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)

# return render_template(
#         "edit_recipe.html", recipe=recipe, categories=categories

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # This is an admin-only page
    user = mongo.db.users.find_one({"username": session["user"]})
    if session['user'] == 'admin':
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name"),
                "category_description": request.form.get(
                    "category_description")
            }
            mongo.db.categories.insert_one(category)
            flash("New category added successfully!")
            return redirect(url_for("get_categories"))
    else:
        flash("This page is for site administrators only")
        return render_template("403.html")

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "category_description": request.form.get("category_description")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category updated successfully!")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category deleted successfully!")
    return redirect(url_for("get_categories"))


# The below functions were guided from
# https://flask.palletsprojects.com/en/2.0.x/errorhandling/#custom-error-pages
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
