from jerry import client

db = client.adb
collection = db.Client


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def find_user(self):
        username_query = {"username": self.username}
        username_exits = collection.find_one(username_query)
        return username_exits

    def log_in(self):
        username_exits = self.find_user()
        password_found = username_exits["password"]
        if self.password == password_found:
            return True
        else:
            return False


class UserCreation(User):

    def __init__(self, username, password, name, last_name, telephone, address, birthday, gender):
        super().__init__(username, password)
        self.name = name
        self.last_name = last_name
        self.telephone = telephone
        self.address = address
        self.birthday = birthday
        self.gender = gender

    def sign_up(self):
        username_exits = self.find_user()
        print(username_exits)
        if username_exits is None:
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
