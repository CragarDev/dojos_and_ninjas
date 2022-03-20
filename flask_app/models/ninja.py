# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


class Ninja:
    # Change Database for this model
    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.dojo = {}

    # UPDATE methods

    @classmethod
    def get_all_ninjas(cls, data):
        print("CLASS METHOD data-id", data["id"])
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query, data)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def show_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def create_new_ninja(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name, age, dojo_id, created_at, updated_at ) VALUES ( %(first_name)s,%(last_name)s,%(age)s, %(dojo_id)s, NOW() , NOW() );"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
