#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
import pymongo as pymongo

jerry_app = Flask(__name__)
uri = "mongodb://adb2018:ulacit2018@ds123929.mlab.com:23929/adb"
client = pymongo.MongoClient(uri)

from jerry.controllers import *
