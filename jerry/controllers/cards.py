from flask import request, jsonify
from jerry import jerry_app
from flask_httpauth import HTTPBasicAuth
from flask import render_template
from ..models.User import User, UserCreation, UserInformation
from ..models import Card
from ..models.User2 import *


@jerry_app.route("/add_cards2", methods=["GET"])
def add_cards2():
    account_number = request.form.get("account_number")
    card_number = request.form.get("card_number")
    cvv = request.form.get("cvv")
    expiration_date = request.form.get("expiration_date")
    account_type = request.form.get("account_type")
    brand = request.form.get("brand")
    password = User3.get_password(self)

    return password
    # add_new_card = Card.Card(account_number, card_number, cvv, expiration_date,
    # account_type, brand, username).add_card()
    # if add_new_card == "Inserted":
    #   return jsonify(add_new_card)
    # else:
    #   return jsonify(add_new_card)
