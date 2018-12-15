import os
import glob
from ..models.User import User

# We load any .py ended file into __all__ so they become discoverable
from flask import request

__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]


def init():
    global username, password, user
    username = request.form.get("username")
    password = request.form.get("password")
    user = User()
