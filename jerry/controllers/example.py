from flask import request, jsonify
from jerry import jerry_app, client

db = client.adb
collection = db.Client


@jerry_app.route("/example", methods=["GET"])
def example():
    return jsonify(db.name)


@jerry_app.route("/city", methods=["GET"])
def get_discipline_city():
    cursor = collection.find()
    vector = []
    for q in cursor:
        print(q)
        vector.append({
            'account': q["account"][1]["account_type"]
        })

    return jsonify(vector)


@jerry_app.route("/test", methods=["GET"])
def get_discipline_test():
    cursor = collection.find()
    vector = []
    for q in cursor:
        print(q)
        vector.append({
            'username': q["username"],
            'password': q["password"]
        })

    return jsonify(vector)


@jerry_app.route("/accounts", methods=["GET"])
def get_account():
    username_query = {"username": "ric"}
    username_exits = collection.find_one(username_query)
    print(username_exits['account'])
    print(len(username_exits['account']))
    vector = []
    for key in username_exits["account"]:
        document = {"ID_CUENTA": key["ID_CUENTA"], "accountNumber": key["accountNumber"],
                    'cardNumber': key["cardNumber"], 'cvv': key["cvv"], "expDate": key["expDate"],
                    "accountType": key["accountType"], "brand": key["brand"]}
        vector.append(document)
    return jsonify(vector)


@jerry_app.route("/accounts", methods=["POST"])
def add_account_example():
    account_number = request.form.get("account_number")
    username = request.form.get("username")

    username_query = {"username": username}
    username_information = collection.find_one(username_query)
    account_list_len = len(username_information['account'])
    if account_list_len == 0:
        new_values = {"$set": {"account." + str(0) + ".id": str(1),
                               "account." + str(0) + ".accountNumber": account_number}}
        print("es : " + str(account_list_len))
        collection.update_one(username_information, new_values)
        return "Inserted"
    else:
        new_id = account_list_len + 1
        new_values = {"$set": {"account." + str(account_list_len) + ".id": str(new_id),
                               "account." + str(account_list_len) + ".accountNumber": account_number}}
        print("es : " + str(account_list_len))
        collection.update_one(username_information, new_values)
        return "Agregado nuevo"



