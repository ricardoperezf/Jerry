from jerry import collection


class Card:

    def __init__(self, account_number, card_number, cvv, expiration_date, account_type, brand, username):
        self.account_number = account_number
        self.card_number = card_number
        self.cvv = cvv
        self.expiration_date = expiration_date
        self.account_type = account_type
        self.brand = brand
        self.username = username

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

    def add_card(self):
        username_query = {"username": self.username}
        username_information = collection.find_one(username_query)
        account_list_len = len(username_information['account'])
        if account_list_len == 0:
            new_values = {"$set": {"account." + str(0) + ".id": str(1),
                                   "account." + str(0) + ".accountNumber": self.account_number,
                                   "account." + str(0) + ".accountType": self.card_number,
                                   "account." + str(0) + ".cvv": self.cvv,
                                   "account." + str(0) + ".expDate": self.expiration_date,
                                   "account." + str(0) + ".accountType": self.account_type,
                                   "account." + str(0) + ".brand": self.brand}}
            print("es : " + str(account_list_len))
            collection.update_one(username_information, new_values)
            return "Inserted"
        else:
            new_id = account_list_len + 1
            new_values = {"$set": {"account." + str(account_list_len) + ".id": str(new_id),
                                   "account." + str(account_list_len) + ".accountNumber": self.account_number,
                                   "account." + str(account_list_len) + ".c": self.card_number,
                                   "account." + str(account_list_len) + ".cvv": self.cvv,
                                   "account." + str(account_list_len) + ".expirationDate": self.expiration_date,
                                   "account." + str(account_list_len) + ".accountType": self.account_type,
                                   "account." + str(account_list_len) + ".brand": self.brand}}
            print("es : " + str(account_list_len))
            collection.update_one(username_information, new_values)
            return "Agregado nuevo"
