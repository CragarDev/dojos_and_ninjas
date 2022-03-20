from flask_app import app

# t- ---- INSERT CONTROLLERS HERE ------------------
from flask_app.controllers import dojos_controller, ninjas_controller

#

#

#
#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
