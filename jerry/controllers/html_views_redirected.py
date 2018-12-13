from flask import request, jsonify, render_template, abort
from jerry import jerry_app


# Set the route and accepted methods
@jerry_app.route('/')
def signin():
    return render_template("signin.html")

@jerry_app.route('/paginasignup')
def signup():
    return render_template("signup.html")

@jerry_app.route('/signout')
def signout():
    return render_template("signup.html")
