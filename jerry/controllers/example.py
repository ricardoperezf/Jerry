from flask import request, jsonify
from jerry import jerry_app, client

db = client.abd
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
            'id': q["id"]
        })

    return jsonify(vector)
