from flask import request, jsonify
from jerry import jerry_app
from flask_httpauth import HTTPBasicAuth
from flask import render_template
from ..models.User import User, UserCreation, UserInformation
from ..models.User2 import *
from ..models.Preference import Preference
from ..models.Card import Card

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


# @jerry_app.route("/add_modify_card", methods=["POST"])
# def add_modify_card():
#    account_number = request.form.get("accountnumber")
#    card_number = request.form.get("cardnumber")
#    cvv = request.form.get("cvv")
#    expiration_date = request.form.get("expdate")
#    account_type = request.form.get("accounttype")
#    brand = request.form.get("brand")
#
#    add_new_card = Card(account_number, card_number, cvv, expiration_date,
#                        account_type, brand, username).add_modify_card()
#    print(add_new_card)
#    if add_new_card == "Modificado":
#       return render_template("index.html"), 201
#    else:
#       return jsonify(add_new_card), 401


@jerry_app.route("/add_cards", methods=["POST"])
def add_cards():
    account_number = request.form.get("account_number")
    card_number = request.form.get("card_number")
    cvv = request.form.get("cvv")
    expiration_date = request.form.get("expiration_date")
    account_type = request.form.get("account_type")
    brand = request.form.get("brand")

    add_new_card = Card().add_card(account_number, card_number, cvv, expiration_date,
                                   account_type, brand, username)
    if add_new_card == "Inserted":
        return render_template("myCards.html")
    else:
        return jsonify(add_new_card)


@jerry_app.route("/get_my_cards", methods=["GET"])
def get_my_cards():
    card_list = Card().get_cards(username)
    if card_list is not None:
        # print(card_list)
        return render_template("myCards.html", get_cards=card_list)
    else:
        return jsonify("There's not exits cards")


@jerry_app.route("/delete_my_cards/<id>", methods=["POST"])
def delete_my_cards(id):
    print(id)
    delete_card = Card().delete_card(username, id)
    if delete_card == "Deleted":
        return render_template("index.html")
    else:
        return jsonify(delete_card)


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
        return render_template("index.html")
    else:
        return jsonify(add_new_preference)


@jerry_app.route("/get_preferences", methods=["GET"])
def get_preferences():
    preference_list = Preference().get_preferences(username)
    if preference_list is not None:
        print(preference_list)
        return render_template("myPreferences.html", get_preferences=preference_list)
    else:
        return jsonify("There's not exits preferences")


@jerry_app.route("/get_information", methods=["GET"])
def user_information():
    information = User().get_user_information(username)
    if information is not False:
        return render_template("myInformation.html", information=information)
    else:
        return jsonify(information)


