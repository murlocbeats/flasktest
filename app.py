from flask import Flask
import hmac
import hashlib
import base64
import requests
import time
import json
import random
import string

app = Flask(__name__)

# Your API key and secret
API_KEY = 'cc_59c730b0f45a7f8f9d7a43483cf09cb1'
API_SECRET = '73b3ad0e84916ce9103c3582d168e88bf1b7cf99376290d0992904c60ab86d73'
API_PASSPHRASE = '13731373'  # Replace with your actual passphrase
prehash_string = 'asfafqfqgqgqg'

@app.route('/')
def home():
    # Generate the current timestamp in milliseconds
    timestamp = int(time.time() * 1000)
    return str(timestamp)

@app.route('/sign')
def generate_signature():
    signature = hmac.new(bytes(API_SECRET, 'utf-8'), bytes(prehash_string, 'utf-8'), hashlib.sha256).digest()
    signature_base64 = base64.b64encode(signature).decode()
    return signature_base64

if __name__ == '__main__':
    app.run(debug=True)
