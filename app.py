from flask import Flask
import hmac
import hashlib
import base64
import requests
import time
import json
import random
import string
from trader import *

app = Flask(__name__)

@app.route('/')
def home():
    # Generate the current timestamp in milliseconds
    timestamp = int(time.time() * 1000)
    return str(timestamp)

@app.route('/sign')
get_single_account()

if __name__ == '__main__':
    app.run(debug=True)
