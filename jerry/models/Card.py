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
            new_values = {"$set": {"account.accountnumber": self.account_number,
                                   "account.cardnumber": self.card_number,
                                   "account.cvv": self.cvv,
                                   "account.expdate": self.expiration_date,
                                   "account.accounttype": self.account_type,
                                   "account.brand": self.brand}}
            insert_user = collection.update_one(find_username, new_values)
            return "Modificado"
        else:
            return False
