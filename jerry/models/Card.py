from jerry import collection


class Card:

    def __init__(self):
        self.account_number = ""
        self.card_number = ""
        self.cvv = ""
        self.expiration_date = ""
        self.account_type = ""
        self.brand = ""
        self.username = ""

    def add_modify_card(self):
        print(self.username)
        if self.username is not None:
            print(self.username)
            find_username = {"username": self.username}
            new_values = {"$": {"account.accountNumber": self.account_number}}
            insert_user = collection.update_one(find_username, new_values)
            return "Modificado"
        else:
            return False

    def add_card(self, account_number, card_number, cvv, expiration_date, account_type, brand, username):
        username_query = {"username": username}
        username_information = collection.find_one(username_query)
        account_list_len = len(username_information['account'])
        document_values = {"account_number": account_number, "card_number": card_number, "cvv": cvv,
                           "expiration_date": expiration_date, "account_type": account_type, "brand": brand}
        print("acc list" + str(account_list_len))
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
                               "account." + str(index_array) + ".account_number": value_list["account_number"],
                               "account." + str(index_array) + ".account_type": value_list["account_type"],
                               "account." + str(index_array) + ".brand": value_list["brand"],
                               "account." + str(index_array) + ".card_number": value_list["card_number"],
                               "account." + str(index_array) + ".cvv": value_list["cvv"],
                               "account." + str(index_array) + ".expiration_date": value_list["expiration_date"]}}
        return new_values

    def get_cards(self, username):
        username_query = {"username": username}
        username_information = collection.find_one(username_query)
        account_list = username_information['account']
        print(account_list)
        return account_list
