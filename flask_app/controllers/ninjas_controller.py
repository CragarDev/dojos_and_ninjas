from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#  3 steps to process form information
#   1. Catch the info in a POST and repackage it to send
#   2. Send the package to a query
#   3. Redirection


# * ===========================================
# ? RENDER / add ninja
# * ===========================================
@app.route("/add_ninja")
def add_ninja():

    all_dojos = Dojo.get_all_dojos()

    return render_template("/add_ninja.html", all_dojos=all_dojos)


# t- ===========================================
# ? PROCESS FORM - / add ninja
# t- ===========================================
@app.route("/add_ninja/new", methods=["POST"])
def add_ninja_new():

    query_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }

    ninja_id = Ninja.create_new_ninja(query_data)

    return redirect("/dojo")
