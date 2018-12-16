from flask import jsonify
from jerry import collection


class Preference:
    def __init__(self):
        self.category = ""
        self.amount = ""
        self.term = ""
        self.username = ""

    def add_preference(self, category, amount, term, username):
        print(self.username)
        username_query = {"username": username}
        username_information = collection.find_one(username_query)
        preferences_list_len = len(username_information['preferences'])
        print(preferences_list_len)
        document_values = {"category": category, "amount": amount, "term": term}
        if preferences_list_len == 0:
            new_values = self.set_new_values(0, 1, document_values)
            collection.update_one(username_information, new_values, document_values)
            return "Inserted"
        else:
            new_id = preferences_list_len + 1
            new_values = self.set_new_values(preferences_list_len, new_id, document_values)
            collection.update_one(username_information, new_values)
        return "Inserted"

    def set_new_values(self, index_array, index_id, value_list):
        new_values = {"$set": {"preferences." + str(index_array) + ".id": str(index_id),
                               "preferences." + str(index_array) + ".amount": value_list["amount"],
                               "preferences." + str(index_array) + ".category": value_list["category"],
                               "preferences." + str(index_array) + ".term": value_list["term"]}}
        return new_values

    def get_preferences(self, username):
        username_query = {"username": username}
        username_information = collection.find_one(username_query)
        preferences_list = username_information['preferences']
        print(preferences_list)
        return preferences_list
