"""
    Code adapted from Code Institute Course Material
    Task Manager Flask App mini Project
"""


import os
from flask_paginate import Pagination, get_page_parameter
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


# Pagination #
PER_PAGE = 8


def paginated(recipes, page):
    offset = page * PER_PAGE - PER_PAGE
    paginated_recipes = recipes[offset: offset + PER_PAGE]
    pagination = Pagination(page=page, per_page=PER_PAGE, total=len(recipes))
    return [
        paginated_recipes,
        pagination
    ]


"""
Render the Home, Article and
all the Footer pages
"""


@app.route("/")
def index():
    # 6 random recipes #
    recipes = mongo.db.recipes
    random_recipes = (
        [recipe for recipe in recipes.aggregate([
            {"$sample": {"size": 6}}])])
    # 3 random products #
    products = mongo.db.products
    random_products = (
        [product for product in products.aggregate([
            {"$sample": {"size": 3}}])])
    return render_template("index.html",
                           page_title="Yummy Recipes",
                           recipes=recipes,
                           random_recipes=random_recipes,
                           products=products,
                           random_products=random_products)


@app.route("/article")
def article():
    return render_template("article.html", page_title="DIY Tips")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact Us")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About Us")


@app.route("/advertising")
def advertising():
    return render_template("advertising.html", page_title="Advertising Policy")


@app.route("/accessibility")
def accessibility():
    return render_template("accessibility.html", page_title="Accessibility")


@app.route("/terms")
def terms():
    return render_template("terms.html", page_title="Terms of Use & Policies")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html", page_title="Privacy Policy")


"""
User account management
"""


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # 3 random products #
    products = mongo.db.products
    random_products = (
        [product for product in products.aggregate([
            {"$sample": {"size": 3}}])])
    """
    Allows the user to create a new account with
    a unique username and password
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("signup"))

        # collect the signup form data and write to MongoDB
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourite_recipes": []
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!", "success")
        # return redirect(url_for("profile", username=session["user"]))
        return redirect(url_for("signup"))

    return render_template("signup.html", page_title="Sign Up",
                           products=products,
                           random_products=random_products)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    # 3 random products #
    products = mongo.db.products
    random_products = (
        [product for product in products.aggregate([
            {"$sample": {"size": 3}}])])
    """
    Allows the user to sign in with username and password.
    Checks for validity of username and password entered.
    Redirects user to profile page after successful login.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                # Welcome message and direct to Profile page
                flash("Welome Back!", "success")
                # return redirect(url_for("profile", username=session["user"]))
                return redirect(url_for("signin"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", "error")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "error")
            return redirect(url_for("signin"))

    return render_template("signin.html", page_title="Sign In",
                           products=products,
                           random_products=random_products)


@ app.route('/signout')
def signout():
    """
    Allows the user to logout and clear the session cookie
    """
    flash("You have been logged out", "success")
    session.pop("user")
    return redirect(url_for('index'))


"""
Recipe CRUD Functionality
"""


@app.route("/all_recipes")
def all_recipes():
    """
    Render the Recipes page for all site visitors
    """
    # Get all recipes from DB #
    recipes = list(mongo.db.recipes.find().sort("_id", -1))
    # Pagination #
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination_obj = paginated(recipes, page)
    paginated_recipes = pagination_obj[0]
    pagination = pagination_obj[1]
    # 3 random products #
    products = mongo.db.products
    random_products = (
        [product for product in products.aggregate([
            {"$sample": {"size": 3}}])])

    return render_template("recipes.html",
                           page_title="All Recipes",
                           recipes=paginated_recipes,
                           recipe_paginated=paginated_recipes,
                           pagination=pagination,
                           products=products,
                           random_products=random_products)


@app.route("/view_recipe/<recipe_id>", methods=["GET", "POST"])
def view_recipe(recipe_id):
    """
    Get the recipe details for the selected recipe and
    render the View Recipe Page
    """
    # Get one recipe from DB #
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # 3 random products #
    products = mongo.db.products
    random_products = (
        [product for product in products.aggregate([
            {"$sample": {"size": 3}}])])
    return render_template("view_recipe.html", recipe=recipe,
                           products=products,
                           random_products=random_products,
                           page_title="Recipe")


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search function
    filters the recipes based on the text index query.
    """
    # Search functionality #
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    # Pagination #
    page = request.args.get(get_page_parameter(), type=int, default=1)
    pagination_obj = paginated(recipes, page)
    paginated_recipes = pagination_obj[0]
    pagination = pagination_obj[1]
    # 3 random products #
    products = mongo.db.products
    random_products = (
        [product for product in products.aggregate([
            {"$sample": {"size": 3}}])])

    return render_template("recipes.html",
                           page_title="Search Result",
                           recipes=recipes,
                           total=len(recipes),
                           recipe_paginated=paginated_recipes,
                           pagination=pagination,
                           search=True,
                           products=products,
                           random_products=random_products)

"""
Subscribe Newsletter Functionality
collect the email address from input field and write to Mongo DB
"""


@app.route('/sub', methods=['POST'])
def sub():
    if request.method == "POST":
        # check if username already exists in db
        existing_email = mongo.db.newsletter.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already exists", "error")
            return redirect(request.referrer)

        sub = mongo.db.newsletter
        return_data = request.form.to_dict()
        sub.insert_one(return_data)
        flash("Successfully Subscribed", "success")
        return redirect(request.referrer)

    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
