from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#  3 steps to process form information
#   1. Catch the info in a POST and repackage it to send
#   2. Send the package to a query
#   3. Redirection


# * ===========================================
# ? RENDER / ninjas
# * ===========================================
@app.route("/dojo_ninjas/<int:dojo_id>")
def dojo_ninjas(dojo_id):
    print("DOJO ID---in dojos and ninjas-", dojo_id)

    query_data = {
        "id": dojo_id
    }
    print("QUERY DATA - id", query_data["id"])

    # all_ninjas = Ninja.get_all_ninjas(query_data)
    dojo = Dojo.get_one_dojo(query_data)

    # print(all_ninjas)
    # for ninja in all_ninjas:
    #     print(ninja.first_name)

    print("Where...DOJOS_NINJAS--READ")
    # return render_template("dojos.html")
    return render_template("dojo_ninjas.html", dojo=dojo)


# * ===========================================
# ? RENDER / add ninja
# * ===========================================
@app.route("/add_ninja")
def add_ninja():
    print("WHERE...ADD NINJA")

    all_dojos = Dojo.get_all_dojos()
    # for dojo in all_dojos:
    #     print(f"Dojo# {dojo.id} Name: {dojo.name}")
    return render_template("/add_ninja.html", all_dojos=all_dojos)


# t- ===========================================
# ? PROCESS FORM - / add ninja
# t- ===========================================
@app.route("/add_ninja/new", methods=["POST"])
def add_ninja_new():

    print("Processing the form- add ninja")
    query_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }

    print("Dojo ID: ", query_data["dojo_id"])
    Ninja.create_new_ninja(query_data)
    print("REDIRECTING to dojos----")
    print("Dojo ID: ", query_data["dojo_id"])
    return redirect("/dojos")
