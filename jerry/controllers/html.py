from flask import request, jsonify, render_template, abort
from jerry import jerry_app, client

db = client.adb
collection = db.Client

# Set the route and accepted methods
@jerry_app.route('/')
def signin():
    return render_template("signin.html")