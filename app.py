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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
