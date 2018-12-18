from jerry import client, collection
from flask import render_template
from passlib.apps import custom_app_context as pwd_context


class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.password_hash = ""

    @staticmethod
    def find_user(username):
        username_query = {"username": username}
        username_exits = collection.find_one(username_query)
        return username_exits

    def log_in(self, username, password):
        username_exits = self.find_user(username)
        if username_exits is not None:
            password_hashed = username_exits['password']
            # print(password_hashed)
            password_verification = self.verify_password(password, password_hashed)
            if password_verification:
                return "Hizo match"
            else:
                return "No hizo match"
        else:
            return "No existe"

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        # print(self.password_hash)
        return self.password_hash

    @staticmethod
    def verify_password(password, password_hashed):
        # return pwd_context.verify(password,
        #                         "$5$rounds=535000$JXpn16YJ58Fw7Rk1$zIEeZXK5h9Y4xd1RKcIh/2kDb8tKnFp.pYJfp6kO55/")
        return pwd_context.verify(password, password_hashed)

    @staticmethod
    def get_user_information(username):
        username_query = {"username": username}
        username_exits = collection.find_one(username_query)
        print(username_exits)
        if username_exits is not None:
            user_information = {"username": username_exits["username"], "name": username_exits["name"],
                                "last_name": username_exits["last_name"], "telephone": username_exits["telephone"],
                                "address": username_exits["address"], "birthday": username_exits["birthday"],
                                "gender": username_exits["gender"]}
            return user_information
        else:
            return False

    def modify_user(self, username, name, last_name, telephone, address, birthday, gender):
        username_query = {"username": username}
        username_exits = collection.find_one(username_query)
        print(username_exits)
        if username_exits is not None:
            document_values = {"username": username,"name": name, "last_name": last_name, "telephone": telephone,
                               "address": address, "birthday": birthday, "gender": gender}
            new_values = self.set_new_values(document_values)
            collection.update_one(username_exits, new_values)
            user_information = {"username": username_exits["username"], "name": username_exits["name"],
                                "last_name": username_exits["last_name"], "telephone": username_exits["telephone"],
                                "address": username_exits["address"], "birthday": username_exits["birthday"],
                                "gender": username_exits["gender"]}
            return user_information
        else:
            return False

    @staticmethod
    def set_new_values(value_list):
        new_values = {"$set": {"username": value_list["username"],
                               "name": value_list["name"],
                               "last_name": value_list["last_name"],
                               "telephone": value_list["telephone"],
                               "address": value_list["address"],
                               "birthday": value_list["birthday"],
                               "gender": value_list["gender"]}}
        return new_values


class UserCreation(User):

    def __init__(self, username, password, name, last_name, telephone, address, birthday, gender):
        super().__init__()
        self.username = username
        self.password = password
        self.name = name
        self.last_name = last_name
        self.telephone = telephone
        self.address = address
        self.birthday = birthday
        self.gender = gender

    def sign_up(self):
        username_exits = self.find_user(self.username)
        print(username_exits)
        if username_exits is None:
            self.password = self.hash_password(self.password)
            new_user_query = {
                "username": self.username,
                "password": self.password,
                "name": self.name,
                "lastname": self.last_name,
                "telphone": self.telephone,
                "address": self.address,
                "birthday": self.birthday,
                "gender": self.gender,
                "account": [],
                "preferences": []
            }
            insert_user = collection.insert_one(new_user_query)
            return render_template("signin.html")
        else:
            return False




class UserInformation:
    def get_user_information(self):
        user_cursor = collection.find()
        vector = []
        for user in user_cursor:
            # print(user)
            vector.append({'name': user["name"], 'lastname': user["lastname"]})
        return vector
