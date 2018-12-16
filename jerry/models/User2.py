from jerry import client, collection
from flask import render_template
from passlib.apps import custom_app_context as pwd_context


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class User2:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.password_hash = ""

    def find_user(self):
        username_query = {"username": self.username}
        username_exits = collection.find_one(username_query)
        return username_exits

    def sign_up(self, name, last_name, telephone, address, birthday, gender):
        username_exits = self.find_user()
        print(username_exits)
        if username_exits is None:
            self.password_hash = pwd_context.encrypt(self.password)
            new_user_query = {"username": self.username, "password": self.password_hash, "name": name,
                              "lastname": last_name, "telphone": telephone, "address": address,
                              "birthday": birthday, "gender": gender, "account": []}
            collection.insert_one(new_user_query)
            return render_template("signin.html")
        else:
            return False

    def log_in(self):
        username_exits = self.find_user()
        if username_exits is not None:
            password_hashed = username_exits['password']
            # print(password_hashed)
            password_verification = pwd_context.verify(self.password, password_hashed)
            if password_verification:
                return "Hizo match"
            else:
                return "No hizo match"
        else:
            return "No existe"

    def get_username(self):
        return self.password


class User3:
    def __init__(self):
        self.username = ""
        self.password = ""

    def set_username(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
