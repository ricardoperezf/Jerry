from flask import request, jsonify
from jerry import jerry_app
from ..models.User import User, UserCreation, UserInformation


def init():
    global username, password, user
    username = request.form.get("username")
    password = request.form.get("password")
    user = User(username, password)


@jerry_app.route("/login", methods=["POST"])
def log_in():
    init()
    user_logged_in = user.log_in()
    if user_logged_in:
        return jsonify(True), 201
    else:
        return jsonify(False), 404


@jerry_app.route("/signup", methods=["POST"])
def sign_up():
    init()
    name = request.form.get("name")
    last_name = request.form.get("last_name")
    telephone = request.form.get("telephone")
    address = request.form.get("address")
    birthday = request.form.get("birthday")
    gender = request.form.get("gender")

    user_not_exits = UserCreation(username, password, name, last_name,
                                  telephone, address, birthday, gender).sign_up()
    if user_not_exits:
        return jsonify(user_not_exits), 201
    else:
        return jsonify(user_not_exits), 401


@jerry_app.route("/user_information", methods=["GET"])
def user_information():
    information = UserInformation().get_user_information()
    return jsonify(information)
