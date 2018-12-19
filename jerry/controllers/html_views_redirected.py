from flask import request, jsonify, render_template, abort
from jerry import jerry_app
from flask import session


# Set the route and accepted methods
@jerry_app.route('/', methods=["GET"])
def signin():
    session["auth"] = 0
    return render_template("signin.html")


@jerry_app.route('/index', methods=["GET"])
def pp():
    return render_template("index.html")


@jerry_app.route('/paginasignup', methods=["GET"])
def signup():
    return render_template("signup.html")
