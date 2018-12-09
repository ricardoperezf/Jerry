from flask import request, jsonify, render_template, abort
from jerry import jerry_app, client

db = client.adb
collection = db.Client

@jerry_app.route("/example", methods=["GET"])
def example():
    return jsonify("Successful")


@jerry_app.route("/city", methods=["GET"])
def get_discipline_city():
    cursor = collection.find()
    vector = []
    for q in cursor:
        print(q)
        vector.append({
            'ID_USUARIO': q["ID_USUARIO"]
        })

    return jsonify(vector)

@jerry_app.route("/test", methods=["GET"])
def get_test():
    cursor = collection.find()
    vector = []
    for q in cursor:
        print(q)
        vector.append({
            'name': q["name"],
            'lastname': q["lastname"]
        })

    return jsonify(vector)

@jerry_app.route("/users", methods=["POST"])
def log_in():
    username = request.form.get("username")
    password = request.form.get("password")

    # print("\n " + str(username) + " " + str(password) + "\n")

    if username is None or password is None:
        # print("entro")
        abort(400)
    return jsonify(password)