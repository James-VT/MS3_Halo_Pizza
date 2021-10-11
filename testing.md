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

