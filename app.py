import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes/<category>")
def get_recipes(category):
     # matches selected category and only displays matching recipes
    if category == "bread":
        recipes = list(mongo.db.recipes.find({"recipe_type": "Bread"}))
    elif category == "cake":
        recipes = list(mongo.db.recipes.find({"recipe_type": "Cake"}))
    elif category == "biscuit":
        recipes = list(mongo.db.recipes.find({"recipe_type": "Biscuit"}))
    
    return render_template("recipes.html", recipes=recipes, category=category)


@app.route("/search", methods=["GET", "POST"])
def search():
     # serches mongo from text input
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    # Displays full recipe page
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("full-recipe.html", recipes=recipes)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        # Loads options already in database and alows user to update them
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {'$set': {
            "recipe_type": request.form.get("recipe_type"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image_url": request.form.get("recipe_image_url"),
            "recipe_prep_time": request.form.get("recipe_prep_time"),
            "recipe_cook_time": request.form.get("recipe_cook_time"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "username": session["user"]
        }})
        
        flash("Recipe Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit-recipe.html", recipes=recipes)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Delete recipe from database
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    username = mongo.db.users.find_one(
        {"name": session["user"]})["name"]
    flash("Recipe Deleted")
    return render_template("profile.html", username=username)



@app.route("/home", methods=["GET", "POST"])
def home():
    # Homepage with another list of recipes
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if email already exists in database
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
       
        if existing_user:
            flash("Email already used")
            return redirect(url_for("register"))

        register = {
            "name": request.form.get("name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("name").lower()
        flash("Registration Successful!")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})


        if existing_user:
            # ensure hashed password matches input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["email"] = request.form.get("email")
                    session["user"] = mongo.db.users.find_one({"email": request.form.get("email")})["name"]
                    
                    flash("Welcome, {}".format(existing_user["name"]))
                    return redirect(url_for("profile", username=session["user"]))
            else:
                #  password/email dont match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))

        else:
            # email doesn't exist
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # find the current users username from database
    username = mongo.db.users.find_one(
        {"name": session["user"]})["name"]
    
    if session["user"]:
        recipes = list(mongo.db.recipes.find())
        return render_template("profile.html", username=username, recipes=recipes)
    
    
    return redirect(url_for("login")) 


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        # adds recipe to database
        recipe = {
            "recipe_type": request.form.get("recipe_type"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image_url": request.form.get("recipe_image_url"),
            "recipe_prep_time": request.form.get("recipe_prep_time"),
            "recipe_cook_time": request.form.get("recipe_cook_time"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "username": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("add_recipe"))
    
    return render_template("add-recipe.html")


@app.route('/logout')
def logout():
    flash("Logged Out")
    session.pop("user")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)



