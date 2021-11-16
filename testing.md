# Testing

## Initial test to ensure this Flask project is correctly set up
To ensure I had the run.py ready to go, I tried to run a simple "Hello, world!" in a browser window. My code, following the instructions from Flask's official documentation and Code Institute's tutorials, looked like this:
```import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
```

Upon opening the port in the CLI, I'm pleased to say the following browser window opened:

![Successful flask test](docs/testing/firstflasktest.png)

---

## Test to ensure the project is connected to MongoDB:
In order to ascertain whether I had properly connected to my MongoDB database for this project, I followed Code Institute's tutorial. My code in run.py looked like this for the function to render the template:

```@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("home.html", recipes=recipes)
```

In my home.html file, I had this:
```
    {% for recipe in recipes %}
        {{ recipe.pizza_name }}<br>
        {{ recipe.category_name }}<br>
        {{ recipe.ingredients }}<br>
        {{ recipe.method }}<br>
        <img src="{{ recipe.image_url }}"><br>
    {% endfor %}
```

Upon opening the project in the console, the page that loaded looked like this:
![Successful MongoDB test](docs/testing/firstmongodbtest.png)

Success!

---

# Feature testing

In this section I shall test the features of the site to ensure they themselves work, and I shall also test these against the user stories to demonstrate which user stories are fulfilled by the existence of these features.

## CRUD functionality

* A big part of this project was the successful implementation of CRUD functionality - create, read, update, delete. I shall start by testing these.

### Create

* A user of this site can upload their recipes for other users and visitors to view, fulfilling the "create" aspect of CRUD. The top of the upload form can be seen below:

![Top half of upload recipe form](docs/testing/featuretesting/crudtesting/createtesting/uploadform1.png)

To test whether the form is acting as it should, we can enter some dummy information and check for it in the database after we've submitted it. Filling in and submitting the form allows us to test a couple of other features at the same time:

1. Add and delete ingredient and cooking step buttons

The form provides functionality for a user to add ingredients for their recipes. One field for this is presented when a user first loads the form page. Beneath this sit two buttons: an "add ingredient" button, and a "delete ingredient" button. A user can click the "add ingredient" button to add an extra ingredient, and do this for all the ingredients they need. Underneath this, the same is true of the "cooking step" field - buttons are present to both add and remove fields for this.

![Ingredient and cooking step fields, and buttons to add and remove extra fields for these](docs/testing/featuretesting/crudtesting/createtesting/adddeletebuttons.png)

And here we can see it again, with more fields added via button clicks:

![Ingredient and cooking step fields with buttons pressed to produce extras](docs/testing/featuretesting/crudtesting/createtesting/buttonspressed.png)

And this time, with fields removed via the delete buttons:

![Delete buttons used to remove fields](docs/testing/featuretesting/crudtesting/createtesting/deletebuttonspressed.png)

The buttons are working fine.

Returning to the form itself, here we have the bottom half of the form. I have now added some dummy data to the form to allow us to test whether it transfers properly to the database. Note that for the image URL field, the form autofills with the data seen here, which links to a generic open-source picture of a pizza from Wikimedia Commons. This is so that a user without a picture for their recipe can be provided with one. Observe the new types of field. We have categories in two forms; one category field is a drop-down menu, and the other exists as a series of checkboxes represented as sliders via a Materialize feature.

![Bottom half of form with category fields](docs/testing/featuretesting/crudtesting/createtesting/bottomhalfofform.png)

We can select items from within the dropdown menu in order to select into which categories each recipe will belong. I could have rolled these in with the Boolean checkboxes below, but as they are slightly more broad in the way the categories work (and person's idea of spicy is not the same as another's, for example; and what defines classic or adventurous is debatable) I have decided to treat these categories differently, allowing them to stand out for content creators as being more relative in terms of how they'd be categorised, as opposed to the attributes mentioned in the sliders which are easily labelled as being true or false. In this case, I have selected only "classic."

![Category menu, with classic selected](docs/testing/featuretesting/crudtesting/createtesting/categorymenu.png)

Beneath the categories, we have the sliders. This is for the person uploading the recipe to be able to relay to a user whether their pizzas are any of the things listed in the image, as these will naturally be pertinent for a user to know. As these are things which run on simple Boolean values, checkboxes seemed the natural way to go.

![Checkbox sliders, with two checked and two unchecked](docs/testing/featuretesting/crudtesting/createtesting/checkboxsliders.png)

We're all set. All that remains now is to click SUBMIT, and then we'll check the database in MongoDB to ensure everything has submitted correctly. This gives us an opportunity to check one other small thing:

2. Flash messages

Upon submitting the recipe, users are returned to the home page and presented with the following flash message:

![Flash message thanking a user for submitting a recipe](docs/testing/flashmessagetest.png)

Great! We know from this that our flash message is working correctly.

And now, over to the database on MongoDB.

3. MongoDB

With our recipe submitted, we would expect to find our recipe in the collection in MongoDB. Sure enough, here we are:

![Image of data successfully having made its way to MongoDB](docs/testing/featuretesting/crudtesting/createtesting/mongodbentry.png)

Great! Everything's uploaded nicely to the database. A few things to note are the data types. Much of the data in the database is held as a string, which you can see from the simple key:value pairs with only a single entry. However, some are held as arrays and have successfully uploaded as such. This includes the ingredients and cooking steps fields, which have successfully received our data, but also the category_name field which is an array with only one item. It can hold more items if a user selects more than one category. Then we have the information from the checkboxes, each of which is stored as a Boolean data type, hence the simple "true" or "false" values for each.

| User story goal achieved by this feature | How as this achieved? |
|---|---|
| 2 Upload their own recipes for others to see. | Users can submit recipes to the site via a link visible to logged-in users in the nav bar. The data they upload is stored in MongoDB. |

This mostly concludes the testing for our "create" functionality. What remains now is to test that it uploads properly to the site itself, which we shall do for our "read" testing, which comes next.

---

### Read

* A visitor to the site will want to read recipes uploaded by other users, and review those uploaded by themselves. This is the R, for "read," in CRUD.

Below is an image of the home page's list of recipes, with the recipe we uploaded during "create" testing included on the bottom right:

![Image of home page recipes with newly uploaded recipe shown](docs/testing/featuretesting/crudtesting/readtesting/homepagereadevidence.png)

And here is an image of the page generated by our code using the information we uploaded earlier:

![Image of the recipe page generated by our uploaded recipe](docs/testing/featuretesting/crudtesting/readtesting/uploadedrecipepage.png)

Everything we entered on that form has appeared as part of the recipe. From here, a user can read all the details of a recipe. However, the information we entered is very thin. So to truly show off the "read" functionality, here's a recipe I uploaded earlier:

![Image of a full recipe page for crud testing evidence](docs/testing/featuretesting/crudtesting/readtesting/fullrecipeview.png)

Note that in the above recipe, in the details section one can find the categories, including the information from the checkboxes, and one can also find who owns/uploaded the recipe. More on that when we reach the update testing, which we'll come to next.

| User story goal achieved by this feature | How as this achieved? |
|---|---|
| 2 Upload their own recipes for others to see. | Once a user has uploaded a recipe, a page to hold that recipe's data is created. This is accessible from the home page and can be viewed by all users on its very own page. |
| 1 Browse pizza recipes and ideas. | A user can find links to recipes from the home page, and upon clicking these cards will be taken to a page where all details on the recipe are presented. |

---

## Bugs

### Navbar on two lines - FIXED

At some point working on the base.html file, the various page links found themselves on two lines, as seen below:

![Navbar links on two lines](docs/testing/bugs/navbarbug.png)

* Finding a solution:
    * After trying out various methods such as altering the padding on each list element, and removing styling from the brand logo, I eventually spotted the missing closing </a> tag on the Account link. Below is the offending line of code, with the closing tag ammended.

```
<li><a href="{{ url_for('account', username=session['user']) }}" class="navbar_text">Account</a></li>
```
Problem solved!
---

### New ingredient fields failing to appear dynamically on button press - FIXED

The page for a user to submit a recipe had an issue with the field for each new ingredient failing to generate when clicked by a user.

![Proto-version of add recipe form, with only one ingredient field](docs/testing/bugs/ingredientbuttonbug.png)

The "Add ingredient" button was registering the click, but no new field was created. The console revealed this:

```
Uncaught TypeError: Failed to execute 'setAttribute' on 'Element': 2 arguments required, but only 1 present.
    at HTMLButtonElement.next_ingredient_button.onclick (script.js:19)
```

Line 19 in script.js revealed the following (line 19 found within the next_ingredient_button.onclick function):
```
nextIngredient.setAttribute('required');
```

So setAttribute was expecting every method to be, essentially, a key:value pair such as ("type", "text"). I wasn't sure how to procede with this, as within the line of HTML for a required form element such as this, one simply puts "required."

* Finding a solution:
    * Inevitably, I ended up on StackOverflow for this one. Specifically, this thread: https://stackoverflow.com/questions/18770369/how-to-set-html5-required-attribute-in-javascript
    * In that thread, they are discussing something slightly different but what set the lightbulb off for me was learning that the "required" attribute is actually a Boolean. Thus, what I should've typed was:

```
nextIngredient.setAttribute('required', 'true');
```

This solved the problem.

---

### Modal failing to open when a user tries to delete a recipe - FIXED

While trying to createa a modal to confirm whether a user really wants to delete their recipe, I came across this problem:

![Image of a bson failure for my modal](docs/testing/bugs/modalfail.png)

Fortunately, plenty of people on the Slack study group have had this same problem. The problem was this:

```
<div class="col s12 center-align">
            {% if session.user|lower == recipe.created_by|lower %}
                <a class="btn-large negative-button-style edit-button modal-trigger" href="RECIPE_DELETE">Delete recipe</a>
                <!-- <a href="{{ url_for('delete_recipe', recipe_id=recipe._id) }}" class="submit btn-large negative-button-style edit-button">
                    Delete recipe <i class="fas fa-trash-alt"></i>
                </a> -->
            {% endif %}
        </div>
        <!--Modal for deleting the recipe-->
        <div id="RECIPE_DELETE" class="modal">
            <div class="modal-content">
                <h4>Confirm deletion</h4>
                <p>Are you sure want to delete this recipe? Once it is deleted, you will be unable to get it back.</p>
            </div>
            <div class="modal_footer">
                <a href="#!" class="modal-close positive-button-style btn-flat">Cancel</a>
                <a href="{{ url_for('delete_recipe', recipe_id=recipe._id) }}" class="modal-close negative-button-style btn-flat">I am sure I want to delete this recipe</a>
            </div>
        </div>
```

The href for the button to open the modal needs a hash symbol in it. I have marked the relevant href here, along with the id to which it must relate, in capital letters. The correct way of solving this is with this in the attributes for the a element that opens the modal:

```
href="#recipe_delete"
```

Problem solved!