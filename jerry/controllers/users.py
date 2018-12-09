from flask import request, jsonify
from jerry import jerry_app
from ..models.User import User, UserInformation


@jerry_app.route("/users", methods=["POST"])
def log_in_():
    username = request.form.get("username")
    password = request.form.get("password")
    user = User(username, password).log_in()
    if user:
        return jsonify(True), 201
    else:
        return jsonify(False), 404


@jerry_app.route("/user_information", methods=["GET"])
def user_information():
    user = UserInformation().get_user_information()
    return jsonify(user)
