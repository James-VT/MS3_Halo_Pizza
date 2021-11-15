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

### New ingredient fields failing to appear dynamically on button press

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

### Modal failing to open when a user tries to delete a recipe

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