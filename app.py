# this file is api and called every minute from google app script

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
from telegram_sender import *


app = Flask(__name__)

@app.route('/')
def home():
    return str(timestamp)

@app.route('/sign')
def sign():
    result = send_message('از ورسل آنلاین هستم!')  # فراخوانی تابع ایمپورت شده
    return result

if __name__ == '__main__':
    app.run(debug=True)


