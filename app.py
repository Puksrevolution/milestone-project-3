"""
    Code adapted from Code Institute Course Material
    Task Manager Flask App mini Project
"""


import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


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
            {"$sample": {"size": 6}}])]
    )
    return render_template("index.html",
                           page_title="Yummy Recipes",
                           recipes=recipes,
                           random_recipes=random_recipes)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact Us")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About Us")


@app.route("/advertising")
def advertising():
    return render_template("advertising.html", page_title="Advertising Policy")


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
