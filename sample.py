
    @classmethod
    def get_faction_with_friends(cls, data):
        query = """SELECT * FROM factions
                    LEFT JOIN friends ON factions.id = friends.faction_id
                    WHERE factions.id = %(faction_id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)

        # step 1) create an instance of your primary info
        # because we did SELECT * FROM factions, "faction" is the primary info, hence why we are in the faction.py
        faction = cls(results[0])  # create instance of faction

        # step 2) collect the data from the JOINED table
        # we joined onto friends, to that is our secondary info that we need to collect. There are multiple, so we need to LOOP
        # ** MAKE SURE that you collect all of the data needed to make an instance!! **
        for data in results:
            friend_data = {
                # on colliding fields that appear in both tables, you have to specify which table the info is coming from. ONLY DO THIS FOR THE REDUNDANT FIELDS
                "id": data["friends.id"],
                # DO NOT put the table name for the fields that only appear in the secondary table
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "occupation": data["occupation"],
                "age": data["age"],
                "created_at": data["friends.created_at"],
                "updated_at": data["friends.updated_at"]
            }

            # step 3) take that collected data and pass it into the related model's class to create an instance.
            friend_instance = friend.Friend(friend_data)

            # step 4) append the new instance into the empty list
            faction.friends.append(friend_instance)

        return faction
