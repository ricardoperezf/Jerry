from flask import request, jsonify
from jerry import jerry_app
from flask_httpauth import HTTPBasicAuth
from flask import render_template
from ..models.User import User, UserCreation, UserInformation
from ..models import Card

auth = HTTPBasicAuth()


def init():
    global username, password, user
    username = request.form.get("username")
    password = request.form.get("password")
    user = User()


@jerry_app.route("/login", methods=["POST"])
def log_in():
    init()
    user_logged_in = user.log_in(username, password)
    if user_logged_in == "Hizo match":
        return render_template("index.html")
    else:
        return jsonify(user_logged_in), 404


@jerry_app.route("/add_modify_card", methods=["POST"])
def add_modify_card():
    account_number = request.form.get("accountnumber")
    card_number = request.form.get("cardnumber")
    cvv = request.form.get("cvv")
    expiration_date = request.form.get("expdate")
    account_type = request.form.get("accounttype")
    brand = request.form.get("brand")

    add_new_card = Card.Card(account_number, card_number, cvv, expiration_date,
                             account_type, brand, username).add_modify_card()
    print(add_new_card)
    if add_new_card == "Modificado":
        return render_template("index.html"), 201
    else:
        return jsonify(add_new_card), 401



@jerry_app.route("/signup", methods=["POST"])
def sign_up():
    init()
    usuario = request.form.get("username")
    contra = request.form.get("password")
    name = request.form.get("name")
    last_name = request.form.get("last_name")
    telephone = request.form.get("telephone")
    address = request.form.get("address")
    birthday = request.form.get("birthday")
    gender = request.form.get("gender")

    user_not_exits = UserCreation(usuario, contra, name, last_name,
                                  telephone, address, birthday, gender).sign_up()
    if user_not_exits:
        return user_not_exits, 201
    else:
        return jsonify(user_not_exits), 401


@jerry_app.route("/user_information", methods=["GET"])
def user_information():
    information = UserInformation().get_user_information()
    return jsonify(information)
