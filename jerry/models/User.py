from jerry import client

db = client.adb
collection = db.Client


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def log_in(self):
        username_query = {"username": self.username}
        username_exits = collection.find_one(username_query)
        password_found = username_exits["password"]
        if self.password == password_found:
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
