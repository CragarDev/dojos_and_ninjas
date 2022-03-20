from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# * ===========================================
# ? RENDER / index
# * ===========================================
@app.route('/')
def index():

    return redirect("/dojos")


# * ===========================================
# ? RENDER / dojos
# * ===========================================
@app.route('/dojos')
def dojos():

    all_dojos = Dojo.get_all_dojos()

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

    return redirect("/dojos")


# * ===========================================
# ? RENDER / dojo - list of ninjas
# * ===========================================
@app.route("/dojo_ninjas/<dojo_id>")
def dojo_ninjas(dojo_id):

    query_data = {
        "dojo_id": dojo_id
    }
    dojo_with_ninjas = Dojo.get_dojo_with_ninjas(query_data)

    return render_template("dojo_ninjas.html", dojo_with_ninjas=dojo_with_ninjas)

# * ===========================================
# ? RENDER / Show all dojos and ninjas
# * ===========================================


@app.route("/show_all")
def show_all():

    show_all_dojos = Dojo.get_all_dojos()
    show_all_ninjas = Ninja.show_all_ninjas()

    return render_template("/show_all.html", show_all_dojos=show_all_dojos, show_all_ninjas=show_all_ninjas)


# * ===========================================
# ? RENDER /
# * ===========================================

# t- ===========================================
# ? PROCESS FORM - /
# t- ===========================================
