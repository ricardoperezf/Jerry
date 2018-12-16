from flask import request, jsonify
from jerry import jerry_app
from flask_httpauth import HTTPBasicAuth
from flask import render_template
from ..models.User import User, UserCreation, UserInformation
from ..models.User2 import *
from ..models.Preference import Preference

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


@jerry_app.route("/add_cards", methods=["POST"])
def add_cards():
    account_number = request.form.get("account_number")
    card_number = request.form.get("card_number")
    cvv = request.form.get("cvv")
    expiration_date = request.form.get("expiration_date")
    account_type = request.form.get("account_type")
    brand = request.form.get("brand")

    add_new_card = Card.Card(account_number, card_number, cvv, expiration_date,
                             account_type, brand, username).add_card()
    if add_new_card == "Inserted":
        return jsonify(add_new_card)
    else:
        return jsonify(add_new_card)


def init_preference():
    global category, amount, term
    category = request.form.get("category")
    amount = request.form.get("amount")
    term = request.form.get("term")


@jerry_app.route("/preferences", methods=["POST"])
def add_preferences():
    init_preference()
    add_new_preference = Preference().add_preference(category, amount, term, username)
    if add_new_preference == "Inserted":
        return jsonify(add_new_preference)
    else:
        return jsonify(add_new_preference)


@jerry_app.route("/preferences", methods=["GET"])
def get_preferences():
    get_preference = Preference().get_preferences(username)
    if get_preference is not None:
        return jsonify(get_preference)
    else:
        return jsonify("There's not exits preferences")


########################################################################


@jerry_app.route("/user_information", methods=["GET"])
def user_information():
    information = UserInformation().get_user_information()
    return jsonify(information)


########################################################################
## TODO LO DEMÁS EN ADELANTE SERÁ DE PRUEBA

def init2():
    global username, password, user2
    username = request.form.get("username")
    password = request.form.get("password")
    user2 = User2(username, password)


@jerry_app.route("/login2", methods=["POST"])
def log_in2():
    init2()
    user_logged_in = user2.log_in()
    if user_logged_in == "Hizo match":
        return render_template("index.html")
    else:
        return jsonify(user_logged_in), 404


@jerry_app.route("/signup2", methods=["POST"])
def sign_up2():
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


def init3():
    global username3, password3, user3
    username3 = request.form.get("username")
    password3 = request.form.get("password")
    user3 = User3()


@jerry_app.route("/login3", methods=["POST"])
def login3():
    init3()
    user3.set_username(username3, password3)
    return user3.get_username()
