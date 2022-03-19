# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    # Change Database for this model
    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # UPDATE methods

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
    def create_new_dojo(cls, data):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    # @classmethod
    # def get_one_user(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(user_id)s;"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     return cls(results[0])

    # @classmethod
    # def update_user(cls, data):
    #     query = "UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s ,updated_at = NOW() WHERE id = %(id)s;"
    #     connectToMySQL(cls.db).query_db(query, data)
    #     return

    # @classmethod
    # def delete_user(cls, data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     connectToMySQL(cls.db).query_db(query, data)
    #     return
