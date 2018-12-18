from jerry import collection
from passlib.hash import cisco_type7


class Card:

    def __init__(self):
        self.account_number = ""
        self.card_number = ""
        self.cvv = ""
        self.expiration_date = ""
        self.account_type = ""
        self.brand = ""
        self.username = ""
        self.account_hash = ""
        self.card_number_hash = ""
        self.cvv_hash = ""
        self.expiration_date_hash = ""
        self.account_type_hash = ""
        self.brand_hash = ""

    def modify_card(self, account_number, card_number, cvv, expiration_date, account_type, brand, username, id):
        username_query = {"username": username}
        username_information = collection.find_one(username_query)
        account_list_len = len(username_information['account'])
        document_values = {"account_number": account_number, "card_number": card_number, "cvv": cvv,
                           "expiration_date": expiration_date, "account_type": account_type, "brand": brand}
        if account_list_len is not None:
            print(self.username)
            username_values = {"username": username, "account.id": id}
            new_values = {"$set": {"account.$.account_number": document_values["account_number"],
                                   "account.$.account_type": document_values["account_type"],
                                   "account.$.brand": document_values["brand"],
                                   "account.$.card_number": document_values["card_number"],
                                   "account.$.cvv": document_values["cvv"],
                                   "account.$.expiration_date": document_values["expiration_date"]}}
            insert_user = collection.update_one(username_values, new_values)
            return "Modificado"
        else:
            return "nada"

    def add_card(self, account_number, card_number, cvv, expiration_date, account_type, brand, username):
        username_query = {"username": username}
        username_information = collection.find_one(username_query)
        account_list_len = len(username_information['account'])
        document_values = {"account_number": account_number, "card_number": card_number, "cvv": cvv,
                           "expiration_date": expiration_date, "account_type": account_type, "brand": brand}
        if account_list_len == 0:
            new_values = self.set_new_values(0, 1, document_values)
            print("es : " + str(account_list_len))
            collection.update_one(username_information, new_values)
            return "Inserted"
        else:
            new_id = account_list_len + 1
            new_values = self.set_new_values(account_list_len, new_id, document_values)
            print("es : " + str(account_list_len))
            collection.update_one(username_information, new_values)
            return "Inserted"

    @staticmethod
    def set_new_values(index_array, index_id, value_list):
        new_values = {"$set": {"account." + str(index_array) + ".id": str(index_id),
                               "account." + str(index_array) + ".account_number": cisco_type7.hash(value_list["account_number"]),
                               "account." + str(index_array) + ".account_type": cisco_type7.hash(value_list["account_type"]),
                               "account." + str(index_array) + ".brand": cisco_type7.hash(value_list["brand"]),
                               "account." + str(index_array) + ".card_number": cisco_type7.hash(value_list["card_number"]),
                               "account." + str(index_array) + ".cvv": cisco_type7.hash(value_list["cvv"]),
                               "account." + str(index_array) + ".expiration_date": cisco_type7.hash(value_list["expiration_date"])}}
        return new_values

    @staticmethod
    def get_cards(username):
        username_query = {"username": username}
        username_information = collection.find_one(username_query)
        account_list = username_information['account']
        solved_list = []
        for i in range(len(username_information['account'])):
            solved_list.append({"account_number": cisco_type7.decode(account_list[i]["account_number"]),
                                "account_type": cisco_type7.decode(account_list[i]["account_type"]),
                                "brand": cisco_type7.decode(account_list[i]["brand"]),
                                "card_number": cisco_type7.decode(account_list[i]["card_number"]),
                                "cvv": cisco_type7.decode(account_list[i]["cvv"]),
                                "expiration_date": cisco_type7.decode(account_list[i]["expiration_date"])})
        # print(account_list)
        return solved_list

    def delete_card(self, username, id):
        username_query = {"username": username}
        username_information = collection.find_one(username_query)
        account_list = username_information['account']
        if account_list is not None:
            account_query = \
                {
                    "$pull":
                        {
                            "account": {"id": id}
                        }
                }
            collection.update(username_query, account_query)
            return "Deleted"
        else:
            return "False"
