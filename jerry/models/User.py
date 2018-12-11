from jerry import client
from passlib.apps import custom_app_context as pwd_context

db = client.adb
collection = db.Client


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
            print(password_hashed)
            password_verification = self.verify_password(password, password_hashed)
            if password_verification:
                return "Hizo match"
            else:
                return "No hizo match"
        else:
            return "No existe"

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        print(self.password_hash)
        return self.password_hash

    def verify_password(self, password, password_hashed):
        # return pwd_context.verify(password,
        #                         "$5$rounds=535000$JXpn16YJ58Fw7Rk1$zIEeZXK5h9Y4xd1RKcIh/2kDb8tKnFp.pYJfp6kO55/")
        return pwd_context.verify(password, password_hashed)


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
                "gender": self.gender
            }
            insert_user = collection.insert_one(new_user_query)
            return True
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
