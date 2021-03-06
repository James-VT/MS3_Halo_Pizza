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

| User story goal achieved by this feature | How was this achieved? |
|---|---|
| 2 Upload their own recipes for others to see. | Users can submit recipes to the site via a link visible to logged-in users in the nav bar. The data they upload is stored in MongoDB. |

### Register function

Users can register an account with the site that allows them to upload and edit their recipes. I include this here as it technically "creates" something: an entry in the database.

| Feature | How to test | Result |
| --- | --- | --- |
| Username and password are required fields and will not accept empty space | Try to submit the form with empty fields | Success - form fails to submit and users are prompted to fill fields. |
| Registering an account | Correctly provide a username and password, then click register | Success - an account is created for the user. |
| Usernames must be unique, and not match an existing one | Attempt to register with an existing username | Success - the user is presented with a flash message informing them that the username already exists, and the form fails to send. |

| User story goal achieved by this feature | How was this achieved? |
|---|---|
| 5 Register with the site to submit recipes. | By the inclusion of a register form |

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

Note that in the above recipe, in the details section one can find the categories, including the information from the checkboxes, and one can also find who owns/uploaded the recipe. More on that when we reach the update testing.

### Browse and view recipes

Users, whether logged in or not, can view recipes on the site.

| Feature | How to test | Result |
| --- | --- | --- |
| The ability to browse all recipes from the home page, via a paginated set of recipes. | Visit the home page, see the recipes, click through the pagination. | Success - four to a page, the recipes present themselves to a user. |
| View a specific recipe | Click on any recipe to view it. | Success - clicking a recipe takes you to a page showing what that recipe is - its steps, its details, its ingredients. |

| User story goal achieved by this feature | How was this achieved? |
|---|---|
| 2 Upload their own recipes for others to see. | Once a user has uploaded a recipe, a page to hold that recipe's data is created. This is accessible from the home page and can be viewed by all users on its very own page. |
| 1 Browse pizza recipes and ideas. | A user can find links to recipes from the home page, and upon clicking these cards will be taken to a page where all details on the recipe are presented. |

---

### Update

* A visitor to the site, having uploaded one or more recipes, may want to edit their recipes.

If a user is logged in to the site and has uploaded a recipe, then when viewing that recipe they will see an extra couple of buttons:

![Image of edit and delete buttons on view recipe page](docs/testing/featuretesting/crudtesting/updatetesting/editdeletebuttons.png)

The purpose of the delete button, we shall come to in the fourth and final section of our CRUD functionality testing. But for now, we shall click on the edit button, which takes us to a familiar-looking page:

![Edit page displayed with auto-filled fields](docs/testing/featuretesting/crudtesting/updatetesting/editpage.png)

Note that in the image above, although we are looking at a similar page to the one via which we uploaded a recipe, we are looking at a different form. This is evidenced by the different page title seen above, and by the auto-filled field in the form. This is achieved by the following bits of code:

* A code example for Materliaze's input fields is below:

```
<input id="pizza_name" name="pizza_name" minlength="4" value="{{ recipe.pizza_name }}" type="text" class="validate" required>
```

Note the double curly brackets surrounding recipe.pizza_name, as we are using Jinja.

* Expected result of above code:
    * Auto-filled input fields for editing. As evidenced in the pictures above and below, this was successful.

---

* A code example for Materialize's text areas:

```
<textarea id="short_description" name="short_description" minlength="5" class="materialize-textarea validate" required>{{ recipe.short_description }}</textarea>
```

For text areas, one should note that the curly brackets go between the opening and closing tags rather than a value field as with the inputs.

* Expected result of above code:
    * Auto-filled text area fields for editing. As evidenced in the pictures above and below, this was successful.

---

* A code example for Materialize's inputs with multiple fields:

```
{% for ingredient in recipe.ingredients %}
    <input id="ingredients" name="ingredients" type="text" class="validate ingredient-input" minlength="4" value="{{ ingredient }}" required>
    <label for="ingredients">Ingredients</label>
{% endfor %}
```

As we have multiple ingredient fields along with multiple cooking step fields, we need to iterate over these to generate as many fields as we have ingredients/cooking steps.

* Expected result of above code:
    * Auto-filled input/text area fields for editing, and as many of these as required. As evidenced in the pictures above and below, this was successful.

---

* A code example for Materialize's select dropdown menus:

```
<select multiple id="category_name" name="category_name" class="validate" required>
    <option value="" disabled>Select one or more</option>
    {% for category in categories %}
        {% if category.category_name in recipe.category_name %}
            <option value="{{ category.category_name }}" selected>{{ category.category_name }}</option>
        {% else %}
            <option value="{{ category.category_name }}">{{ category.category_name }}</option>
        {% endif %}
    {% endfor %}
</select>
<label for="category_name" class="label-text">Pizza categories</label>
```

For this recipe, we would expect only the "classic" category to be found auto-filled within the field.

* Expected result of above code:
    * Autofilled select dropdown, in this case containing only the "classic" category. As evidenced by the picture below, this was successful.

---

* A code example for Materialize's checkboxes, autofilled from the Booleans held in our database:

```
<div class="switch">
    <i class="fas fa-egg prefix icon-hide"></i>
    <label for="is_vegetarian">
        {% if recipe.is_vegetarian %}
            <input type="checkbox" id="is_vegetarian" name="is_vegetarian" checked>
        {% else %}
            <input type="checkbox" id="is_vegetarian" name="is_vegetarian">
        {% endif %}
        <span class="lever"></span>
        Vegetarian
    </label>
</div>
```

Here I have demonstrated only the vegetarian checkbox, as it is indicative of the others.

* Expected result of above code:
    * Auto-checked boxes filled from our database's Boolean values. As evidenced by the picture below, this was successful.

---

And here is the evidence of the lower half of the form:

![Evidence of lower half of form with auto-filled fields](docs/testing/featuretesting/crudtesting/updatetesting/editpagebottom.png)

---

Now I will test that the edit form is working by changing a few things. We'll remove an ingredient, add a cooking step, add a category and uncheck one checkbox. The result looks like this:

![Edited form with changed fields and data](docs/testing/featuretesting/crudtesting/updatetesting/editedrecipeform.png)

A user at this stage has two options. They can either submit the changes, or cancel them using the appropriate buttons at the bottom of the page. If we click the cancel button, we'd expect to be taken back to the home page and away from the edit form. This is performed by this piece of code the HTML:

```
<a href="{{ url_for('get_recipes') }}" class="btn-large negative-button-style">
    Cancel edit <i class="fas fa-times-circle right"></i>
</a>
```

Between the curly brackets in the code above, we're using Jinja to call the following function from our Python app.py file:

```
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("home.html", recipes=recipes)
```

This function takes us to our home page, as demonstrated by the results of us clicking the cancel edit button, seen below:

![The URL of the page to which our cancel button has taken us](docs/testing/featuretesting/crudtesting/updatetesting/cancelbuttonroute.png)

In the above picture you can see the URL we were taken to upon clicking the cancel button - it is our home page.

But to test the form itself, we are going to click the edit pizza button instead. Having done this, I first get a flash message confirming what I've done. That can be seen here:

![Image of flash message shown after updating a recipe](docs/testing/featuretesting/crudtesting/updatetesting/recipeupdatedflash.png)

And now we can check the databse. Having made editions, we would expect to find the corresponding entry in the database changed to reflect the editions. And here they are:

![Image of the changes in the database](docs/testing/featuretesting/crudtesting/updatetesting/editeddbentry.png)

Fantastic! The changes we made to the recipe have manifested themselves in the database. So if we now check the recipe page, we see this:

![Image of recipe page with editiions successfully showing](docs/testing/featuretesting/crudtesting/updatetesting/editedrecipepage.png)

Excellent! As expected, the changes have successfully been made via the edit recipe form, have gone from this to the database and from the database, they now show on the recipe's page on our site. Our update functionality is working as expected!

| User story goal achieved by this feature | How was this achieved? |
|---|---|
| 3 Edit their submitted recipes. | Users are able to see the "edit" button on recipes they themselves have uploaded. Changes made to their recipes alter what is held in the database, and the corresponding recipe page changes to reflect these editions. |

---

### Delete

* A user of the site, having submitted one or more recipes, may wish to delete them from the site.

If a user is logged in to the site and has uploaded a recipe, then when viewing that recipe they will see an extra couple of buttons, as has been established. We will focus on the delete button:

![Image of the edit and delete buttons on a recipe, visible only to the recipe owner](docs/testing/featuretesting/crudtesting/updatetesting/editdeletebuttons.png)

Clicking this button presents the user with a little defensive programming: a modal asking them if they're sure they wish to delete the recipe. This is pictured below:

![Image of the confirmation modal that's triggered when a user tries to delete a recipe](docs/testing/featuretesting/crudtesting/deletetesting/confirmdeletemodal.png)

Clicking the button to cancel the deletion simply closes the modal. To delete the modal, we need to click the button that says "I am sure I want to delete this recipe." Once this button is clicked, the entrire recipe will be removed from the database collection, and so will be irretrievable. So to test this works, I shall click the button. These steps are recorded below.

1. Ensure you are logged in and are viewing a recipe you have uploaded.
2. Click the red "delete recipe" button.
3. In the modal that appears, click the button that says "I am sure I want to delete this recipe."
4. The expected result is that this wil delete the recipe.

Evidence of result:

![Evidence of the recipe page with our deleted recipe missing](docs/testing/featuretesting/crudtesting/deletetesting/recipegone.png)

Result: success! As you can see from the image, where once there were four recipes there are now three!

| User story goal achieved by this feature | How was this achieved? |
|---|---|
| 4 Delete their submitted recipes. | Users can delete their recipes via the delete function, visible to them on recipes they have uploaded to the site. |

---

### Create, edit, and delete categories as an admin

An admin can create categories by which recipes can be grouped, and subsequently viewed by visitors. This is yet further CRUD functionality, along the same lines as that above, so I include it here in a briefer format to demonstrate the testing of it.

| Feature | How to test | Result |
| --- | --- | --- |
| Create category | As admin, click "Browse categories." Buttons will be visible to you in here that are not visible to visitors. Click "Add category," enter the data for the category you wish to create, and click to confirm. You can then view this new category's entry in the database, and see it on the "Browse categories" page. | Success - a new category is created in the database and on the "Browse categories" page, and is selectable when uploading or editing a recipe. Users also receive a flash message confirming what they've done. |
| Edit category | As admin, click "Browse categories." Buttons will be visible to you in here that are not visible to visitors. Click "Edit category" from any category, alter the data for the category you wish to change, and click to confirm. You can then view this category's updated entry in the database, and see its changes on the "Browse categories" page. | Success - the changes are visible in the category's name and/or description, and in the database. Action confirmed to user via flash message. |
| Delete category | As admin, click "Browse categories." Buttons will be visible to you in here that are not visible to visitors. Click "Delete category" from any category, and click the button in the modal to confirm. This entry is then permanently removed from the database. | Success - the category is gone from the database. Action confirmed to user via flash message. |

---

## Other features

### Log in/out function

Users with accounts can log in to the site after having been away from it.

| Feature | How to test | Result |
| --- | --- | --- |
| Username and password are required fields and will not accept empty space | Try to submit the form with empty fields | Success - form fails to submit and users are prompted to fill fields. |
| Logging in to the site | Enter your username and password into the appropriate fields. Click the button to log in. | Success - user is logged in. |
| Log out of the site | Having logged in, click the log out option in the bar. | Success - user is logged out. |

---

### Search function

The site features a search bar on its home page, by which users can search for keywords in certain sections of the site. For example, below is an image of the search bar with the word "egg" typed into it.

![Image of search bar with egg typed into it.](docs/testing/featuretesting/crudtesting/locatetesting/eggsearchbar.png)

I can test this works by clicking the "search" button. (The reset button clears the entry and refreshes the page. This can be testing by clicking it.) If I click the search button, here's what I am presented with:

![Image of egg search results](docs/testing/featuretesting/crudtesting/locatetesting/eggsearchresults.png)

We see these three recipes. On clicking one of them, I can confirm that it contains not just one egg, but two:

![Image of recipe with egg ingredient](docs/testing/featuretesting/crudtesting/locatetesting/eggingredient.png)

This is great, as it shows the terms do not have to be exact, and can contain only part of a word and still work. Success!

---

# Testing against user stories

In this section we will test each user story against the features of the site to ensure that every one is met. Although some user stories are already mentioned in the feature testing above, I present this as something of a summary to serve as a check list that all user needs are met for certainty's sake.

## A visitor to the site will want to:

| User story number | A user will want to: | How was this achieved? | Evidence of user story having been met |
|--- | --- | --- | --- |
| 1 | Browse pizza recipes and ideas. | Pizzas can be browsed as a complete, paginated list from the home page, and by category from the "browse categories" page, and a user can browse their own creations. | [Image of the main page of the site, and the recipes displayed](docs/testing/featuretesting/crudtesting/readtesting/homepagereadevidence.png) |
| 2 | Upload their own recipes for others to see. | Users, when signed into the site, can upload their recipes by clicking the "submit recipe" button. | [Form for uploading a recipe](docs/testing/featuretesting/crudtesting/createtesting/uploadform1.png) |
| 3 | Edit their submitted recipes. | Users can see, when viewing their own pages, a button allowing them to edit the recipe. On clicking this form, they are taken to a form to update the recipe. | [Form for editing recipes](docs/testing/featuretesting/crudtesting/updatetesting/editpage.png), [Buttons for editing and deleting a recipe](docs/testing/featuretesting/crudtesting/updatetesting/editdeletebuttons.png) |
| 4 | Delete their submitted recipes. | A button exists to confirm with a user that they want to delete their recipes. On clicking this, a modal appears to confirm this decision. | [Buttons for editing and deleting a recipe](docs/testing/featuretesting/crudtesting/updatetesting/editdeletebuttons.png) |
| 5 | Register with the site to submit and edit recipes. | Visitors can register an account with the site by which they can access member functionality, which includes the uploading and editing of recipes. | [Register form](docs/testing/featuretesting/userstorytesting/registerform.png) |
| 6 | View recipes without having to register for the site or log in. | All recipes can be viewed without being logged in. | [Recipe card with log in and register links visible](docs/testing/featuretesting/userstorytesting/notloggedinhomepage.png) |


## A site owner will want to:

| User story number | A user will want to: | How was this achieved? | Evidence of user story having been met |
|--- | --- | --- | --- |
| 7 | Receive on-screen confirmation that my creations, editions and deletions have been successful, and for the visitors to also receive these where appropriate. | Flash messages for interactions including logging in, uploading a recipe, editing a recipe, deleting a recipe and all this functionality for categories if site admin. | [Flash messages displayed for various data-handling functions such as creating, editing and deleting recipes](docs/testing/flashmessagetest.png), [Message confirming category deleted](docs/testing/featuretesting/userstorytesting/deleteflash.png) |
| 8 | Create recipe categories to group recipes. | This can be done as admin from the "Browse by category" page. | [Category card of admin-created category](docs/testing/featuretesting/userstorytesting/addcategoryevidence.png), [Entry for created category in database](docs/testing/featuretesting/userstorytesting/newcategoryindb.png), [Form for adding categories](docs/testing/featuretesting/userstorytesting/addcategoryform.png) |
| 9 | Edit recipe categories. | This can be done as admin from the "Browse by category" page. | [Form for editing recipes](docs/testing/featuretesting/userstorytesting/editcategoryform.png) |
| 10 | Delete recipe categories. | This can be done as admin from the "Browse by category" page. | [Buttons with options for editing, deleting and viewing categories](docs/testing/featuretesting/userstorytesting/categoryvieweditdelete.png), [Modal to confirm the deletion of a category](docs/testing/featuretesting/userstorytesting/deletecategorymodal.png), [Message confirming category deleted](docs/testing/featuretesting/userstorytesting/deleteflash.png) |
| 11 | Allow users to log in so they can submit recipes, hopefully encouraging return visits. | Users can log in via a link on the home page, taking them to a form. | [Image of home page with log in functionality visible](docs/testing/featuretesting/userstorytesting/notloggedinhomepage.png). [Image of the log in form](docs/testing/featuretesting/userstorytesting/loginform.png) |
| 12 | Delete users' recipes if required. | Aside from the users to whom the recipes belong, the only person to be able to delete them is the admin. | [Button for deleting a recipe](docs/testing/featuretesting/userstorytesting/admindelete.png) |
| 13 | Restrict access to certain features to be solely for the site admin. | Code in the right places ensures only the admin can access certain features, such as editing or deleting categories. | [Code restricting access to certain features to only an admin](docs/testing/featuretesting/userstorytesting/adminonlycode.png) |

---

## Validators

### Lighthouse

Home page

![Lighthouse home page validator evidence](docs/testing/validators/homepagelighthouse.png)

Browse by category page

![Category page validator evidence](docs/testing/validators/categorypagelighthouse.png)

Account page

![Account user recipes validator evidence](docs/testing/validators/accountpagelighthouse.png)

Add category page

![Add category page validator evidence](docs/testing/validators/addcategorylighthouse.png)

Edit category page

![Edit category page validator evidence](docs/testing/validators/editcategorylighthouse.png)

Upload recipe page

![Upload recipe page validator evidence](docs/testing/validators/uploadrecipelighthouse.png)

Edit recipe page

![Edit recipe page validator evidence](docs/testing/validators/editrecipelighthouse.png)

Log in page

![Log in validator evidence](docs/testing/validators/registerformlighthouse.png)

Register page

![Register page validator evidence](docs/testing/validators/registerformlighthouse.png)

View by category page

![View by category page validator evidence](docs/testing/validators/viewbycategorylighthouse.png)

View recipe page

![View recipe page validator evidence](docs/testing/validators/recipepagelighthouse.png)

---

### Jigsaw

Jigsaw is used to validate CSS code. Below is evidence of my clean CSS code.

![Evidence of CSS Jigsaw validation](docs/testing/validators/jigsawvalidator.png)

---

### JS Hint

JS Hint is an online validator for JavaScript code. For this project we have two JS files: addeditjs.js and script.js. First is evidence of the successful validation of our addeditjs.js code:

![Evidence of addeditjs.js validation](docs/testing/validators/jshintaddeditvalidator.png)

And now our script.js file:

![Evidence of script.js validation](docs/testing/validators/scriptjsvalidation.png)

### PEP8

PEP8 is a standard by which Python code can be measured for consistent standards of indentation among other things. I ran my app.py file through it and it was given the all clear.

![All right from PEP8](docs/testing/validators/pep8validator.png)

---

## Responsiveness

This site features many media queries to allow it to appear consistently at all screen sizes. I have done this using dev tools (to do this, right click on any page, click Inspect, then along the new bar at the top of the page select the device you'd like to emulate or select responsive and then click and drag the sides), my own two monitors, two separate desktop monitors at work and my Samsung Galaxy S5. To assist in ensuring continuity across browsers, I have enlisted the help of AutoPrefixer (credit in Technologies Used).

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

---

### Validator testing falling short

[Validator testing for upload recipe form](docs/testing/validators/uploadrecipelighthouse.png)

![Edit recipe page validator evidence](docs/testing/validators/editrecipelighthouse.png)

As you can see, the upload form scores only 89% for accessibility. This is deeply frustrating as the solution it mentions - to include a label tag - is already fulfilled. If time allowed, I would investigate this further but for now it is an unsolved bug.

The latter problem is also tedious, as the fields are dynamically generated for extra ingredients and cooking steps. The identical labels on these are causing it to fail, but for the functionality and uploading this is necessary.

---

### Unable to paginate search results - FIXED VIA WORKAROUND

An irritating bug was found when trying to implement pagination for search results. Our pagination allows for 4 results per page. To see any recipes after those first four, you click to see them via the pagination controls.

However, the creation of the Index page with search results requires a re-sending of the search term. Without this being done, it creates an error. This is hard to implement defensively, as if a user has changed it it will create an error and re-generating the page with the search term in the bar was re-sending the search and landing us back at page one. With more time, a better solution could probably be found but for now, our solution is to create a separate template called searchresults.html and not implement pagination on that page. This ensures an error-free user experience in the mean time.
