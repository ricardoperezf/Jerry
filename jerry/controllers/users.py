from flask import request, jsonify
from jerry import jerry_app
from flask_httpauth import HTTPBasicAuth
from flask import render_template
from ..models.User import User, UserCreation, UserInformation
from ..models.User2 import *
from ..models.Preference import Preference
from ..models.Card import Card
from flask import session
from email.mime import application

auth = HTTPBasicAuth()

jerry_app.secret_key = "-S;A792[Qr7muHVGqDj6NTkrP8vk5jP&5_&Ki+AWyJYp(bX{D]3%yhXX8x%gyf!UeVy.nvPL]Tua.+JS}Pc5tRPCX_+GD:8B?aNwyM+BVG_Jj;32[@E8@Yb+Uq#dEXh4e:aYER&%h,}D7Y_e].Tq4Q4bX-2;796Lb*ewnP8Y,djGT3p#R$]WeLV($annmje7B:G}i{{_2Kr7tH2/U%n=2iw@W,cN]RzRCVgMTRYh;_}2fK{Z*%Yzn94Rwa(-Z-y+jhiy95R2#4{/$/KtCT_j2T6:rggrhyA-n)3y=%#*RuLy"


# jerry_app.config['SESSION_TYPE'] = 'filesystem'

def init():
    global username, password, user
    username = request.form.get("username")
    password = request.form.get("password")
    user = User()


def init_username():
    global user, password
    session["user"] = request.form.get("username")
    session["pass"] = request.form.get("password")
    user = User()


@jerry_app.route("/login", methods=["POST"])
def log_in():

    if session["user"] is not None and session["auth"] == 1:
        return render_template("index.html")
    else:


        init_username()

        print("sessi " + session["pass"])

        user_logged_in = user.log_in(session["user"], session["pass"])

        if user_logged_in == "Hizo match":
            # print(session["user"])
            session["auth"] = 1
            return render_template("index.html")
        else:
            # print(user_logged_in)
            return render_template("signin.html", login=user_logged_in)


@jerry_app.route("/logout", methods=["GET"])
def log_out():
    # session.clear()
    # session.pop('user', None)
    # session.pop('password', None)
    # print(sess)
    session["user"] = None
    session["pass"] = None
    session["auth"] = 0

    # session.Abandon()
    return render_template("signin.html")


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
    if user_not_exits == "Not exits":
        return render_template("signin.html")
    else:
        return render_template("signup.html", user_exits=user_not_exits)


@jerry_app.route("/add_cards", methods=["POST"])
def add_cards():
    if session["auth"] == 0:
        return render_template("signin.html")

    account_number = request.form.get("account_number")
    card_number = request.form.get("card_number")
    cvv = request.form.get("cvv")
    expiration_date = request.form.get("expiration_date")
    account_type = request.form.get("account_type")
    brand = request.form.get("brand")

    add_new_card = Card().add_card(account_number, card_number, cvv, expiration_date,
                                   account_type, brand, session["user"])
    if add_new_card == "Inserted":
        return render_template("myCards.html")
    else:
        return jsonify(add_new_card)


@jerry_app.route("/modifycard", methods=["POST"])
def modify_Card():
    if session["auth"] == 0:
        return render_template("signin.html")

    account_number = request.form.get("account_number2")
    card_number = request.form.get("card_number2")
    cvv = request.form.get("cvv2")
    expiration_date = request.form.get("expiration_date2")
    account_type = request.form.get("account_type2")
    brand = request.form.get("brand2")
    id = request.form.get("id")

    add_new_card = Card().modify_card(account_number, card_number, cvv, expiration_date,
                                      account_type, brand, session["user"], id)
    if add_new_card == "Modificado":
        return render_template("myCards.html")
    else:
        return jsonify(add_new_card)


@jerry_app.route("/modifyPreference", methods=["POST"])
def modify_Preference():
    if session["auth"] == 0:
        return render_template("signin.html")

    category = request.form.get("category2")
    amount = request.form.get("amount2")
    term = request.form.get("term2")
    id = request.form.get("id")
    add_new_card = Preference().modify_preference(category, amount, term, session["user"], id)
    if add_new_card == "Modificado":
        return render_template("index.html")
    else:
        return jsonify(add_new_card)


@jerry_app.route("/modify", methods=["POST"])
def modify_User():
    if session["auth"] == 0:
        return render_template("signin.html")

    name = request.form.get("name")
    last_name = request.form.get("last_name")
    telephone = request.form.get("telephone")
    address = request.form.get("address")
    birthday = request.form.get("birthday")
    gender = request.form.get("gender")

    add_new_card = User().modify_user(session["user"], name, last_name, telephone,
                                      address, birthday, gender)
    information = User().get_user_information(session["user"])
    if information is not False:
        return render_template("myInformation.html", information=information)
    else:
        return jsonify(add_new_card)


@jerry_app.route("/get_my_cards", methods=["GET"])
def get_my_cards():
    if session["auth"] == 0:
        return render_template("signin.html")

    card_list = Card().get_cards(session["user"])
    if card_list is not None:
        # print(card_list)
        return render_template("myCards.html", get_cards=card_list)
    else:
        return jsonify("There's not exits cards")


@jerry_app.route("/delete_my_cards/<id>", methods=["POST"])
def delete_my_cards(id):
    if session["auth"] == 0:
        return render_template("signin.html")

    print(id)
    delete_card = Card().delete_card(session["user"], id)
    if delete_card == "Deleted":
        return render_template("index.html")
    else:
        return jsonify(delete_card)


@jerry_app.route("/delete_my_preferences/<id>", methods=["POST"])
def delete_my_preferences(id):
    if session["auth"] == 0:
        return render_template("signin.html")

    print(id)
    delete_card = Preference().delete_preferences(session["user"], id)
    if delete_card == "Deleted":
        return render_template("index.html")
    else:
        return jsonify(delete_card)


def init_preference():
    if session["auth"] == 0:
        return render_template("signin.html")

    global category, amount, term
    category = request.form.get("category")
    amount = request.form.get("amount")
    term = request.form.get("term")


@jerry_app.route("/preferences", methods=["POST"])
def add_preferences():
    if session["auth"] == 0:
        return render_template("signin.html")

    category = request.form.get("category")
    amount = request.form.get("amount")
    term = request.form.get("term")
    add_new_preference = Preference().add_preference(category, amount, term, session["user"])
    print("pref" + add_new_preference)
    if add_new_preference == "Inserted":
        return render_template("index.html")
    else:
        return jsonify(add_new_preference)


@jerry_app.route("/get_preferences", methods=["GET"])
def get_preferences():
    if session["auth"] == 0:
        return render_template("signin.html")

    preference_list = Preference().get_preferences(session["user"])
    if preference_list is not None:
        print(preference_list)
        return render_template("myPreferences.html", get_preferences=preference_list)
    else:
        return jsonify("There's not exits preferences")


@jerry_app.route("/get_information", methods=["GET"])
def user_information():
    if session["auth"] == 0:
        return render_template("signin.html")

    information = User().get_user_information(session["user"])
    if information is not False:
        return render_template("myInformation.html", information=information)
    else:
        return jsonify(information)


@jerry_app.route("/modify_information", methods=["POST"])
def modify_information():
    if session["auth"] == 0:
        return render_template("signin.html")

    username = request.form.get("username")
    name = request.form.get("name")
    last_name = request.form.get("last_name")
    telephone = request.form.get("telephone")
    address = request.form.get("address")
    birthday = request.form.get("birthday")
    gender = request.form.get("gender")

    print(username)
    print(name)
    print(last_name)
    print(telephone)
    print(address)
    print(birthday)
    print(gender)

    modify_user = User().modify_user_information(username, name, last_name, telephone, address, birthday, gender)
    return jsonify(modify_user)
