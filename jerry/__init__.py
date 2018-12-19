#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
import pymongo as pymongo

jerry_app = Flask(__name__)
uri = "mongodb://localhost:27017/adb"
client = pymongo.MongoClient(uri)
db = client.adb
collection = db.Client

from jerry.controllers import *
