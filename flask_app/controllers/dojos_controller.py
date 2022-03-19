from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo


# * ===========================================
# ? RENDER / index
# * ===========================================
@app.route('/')
def index():

    print("Where...HOME--READ")
    return render_template("index.html")


# * ===========================================
# ? RENDER / dojos
# * ===========================================
@app.route('/dojos')
def dojos():

    all_dojos = Dojo.get_all_dojos()

    print(all_dojos)
    for dojo in all_dojos:
        print(dojo.name)

    print("Where...DOJOS--READ")
    # return render_template("dojos.html")
    return render_template("dojos.html", all_dojos=all_dojos)


# t- ===========================================
# ? PROCESS FORM - / create dojo
# t- ===========================================
@app.route("/dojo_new", methods=["POST"])
def dojo_new():

    if request.form["name"] == "":
        return redirect("/dojos")

    query_data = {
        "name": request.form["name"]
    }

    Dojo.create_new_dojo(query_data)

    print("Where...CREATE DOJO")
    return redirect("/dojos")


# * ===========================================
# ? RENDER /
# * ===========================================

# t- ===========================================
# ? PROCESS FORM - /
# t- ===========================================
