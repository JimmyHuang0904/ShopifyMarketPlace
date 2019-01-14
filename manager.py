#!/usr/bin/env python3

import os

from flask import Flask


env = os.environ.get('MARKETPLACE_ENV', 'dev')
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, World!'
