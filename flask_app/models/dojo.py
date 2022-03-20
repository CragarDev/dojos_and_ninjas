# import the function that will return an instance of a connection

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    # Change Database for this model
    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])
        return dojo

    @classmethod
    def create_new_dojo(cls, data):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """SELECT * FROM dojos
                   LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
                   WHERE dojos.id = %(dojo_id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])
        for data in results:
            ninja_data = {
                "id": data["ninjas.id"],
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "age": data["age"],
                "dojo_id": data["dojo_id"],
                "created_at": data["ninjas.created_at"],
                "updated_at": data["ninjas.updated_at"],
            }
            ninja_instance = ninja.Ninja(ninja_data)
            dojo.ninjas.append(ninja_instance)
        return dojo
