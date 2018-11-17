#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
import pymongo as pymongo

jerry_app = Flask(__name__)
uri = "mongodb://abd2018:ulacit2018@ds041167.mlab.com:41167/abd"
client = pymongo.MongoClient(uri)

from jerry.controllers import *
