from flask import request, jsonify, render_template, abort
from jerry import jerry_app


# Set the route and accepted methods
@jerry_app.route('/', methods=["GET"])
def signin():
    return render_template("signin.html")


@jerry_app.route('/index', methods=["GET"])
def pp():
    return render_template("index.html")


@jerry_app.route('/paginasignup', methods=["POST"])
def signup():
    return render_template("signup.html")


@jerry_app.route('/signout', methods=["GET"])
def signout():
    return render_template("signin.html")

@jerry_app.route('/add_cards',methods=["GET"])
def add_card_view():
    return render_template("AñadirTarjeta.html")


@jerry_app.route('/add_modify_card')
def modify_card_view():
    return render_template("CambiarTarjeta.html")
