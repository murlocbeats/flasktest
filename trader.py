import hmac
import hashlib
import base64
import requests
import time
import json
import random
import string
from telegram_sender import *

# Your API key and secret
API_KEY = 'cc_59c730b0f45a7f8f9d7a43483cf09cb1'
API_SECRET = '73b3ad0e84916ce9103c3582d168e88bf1b7cf99376290d0992904c60ab86d73'
API_PASSPHRASE = '13731373'  # Replace with your actual passphrase

# Generate the current timestamp in milliseconds
timestamp = int(time.time() * 1000)

def generate_signature(prehash_string):
    signature = hmac.new(bytes(API_SECRET, 'utf-8'), bytes(prehash_string, 'utf-8'), hashlib.sha256).digest()
    signature_base64 = base64.b64encode(signature).decode()
    return signature_base64
    
#Generate random string
def generate_random_string(length=9):
    # مجموعه کاراکترهای مجاز شامل حروف بزرگ، حروف کوچک و اعداد
    characters = string.ascii_letters + string.digits
    # تولید رشته تصادفی با استفاده از انتخاب تصادفی از مجموعه کاراکترهای مجاز
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def place_order(coin='BTCUSDT_UMCBL', size='0.001', side='open_long', presetTakeProfitPrice='', presetStopLossPrice=''):
    # API endpoint for placing orders
    url = 'https://api.coincatch.com/api/mix/v1/order/placeOrder'

    #Generate client_oid
    client_oid = "unique_client_order_id" + generate_random_string()
    print('client_oid: ' + client_oid)

    # Create the order payload
    order = {
        "symbol": coin,
        "size": str(size),  # Adjust the size as needed | min size = '0.001'
        "side": side,
        "orderType": "market",  # Assuming a market order; change to "limit" if needed
        "marginCoin": "USDT",
        "presetTakeProfitPrice": str(presetTakeProfitPrice),
        "presetStopLossPrice": str(presetStopLossPrice),
        "client_oid": client_oid  # Replace with a unique client order ID
    }


    # Convert the order payload to JSON format
    body = json.dumps(order)

    # Create the prehash string
    prehash_string = f'{timestamp}POST/api/mix/v1/order/placeOrder{body}'

    # Generate the signature
    signature_base64 = generate_signature(prehash_string)

    # Create the headers
    headers = {
        'ACCESS-KEY': API_KEY,
        'ACCESS-SIGN': signature_base64,
        'ACCESS-TIMESTAMP': str(timestamp),
        'ACCESS-PASSPHRASE': API_PASSPHRASE,
        'Content-Type': 'application/json'
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, data=body)

    #send to telegram
    send_message('place_order: ' + '\n' + 'status_code: ' + str(response.status_code) + '\n' + 'msg: ' + response.json()['msg'])

    # Print the response
    print(response.status_code)
    print(response.json())

def get_all_position():
    # API endpoint for placing orders
    url = 'https://api.coincatch.com/api/mix/v1/position/allPosition-v2?productType=umcbl'

    #Generate client_oid
    client_oid = "unique_client_order_id" + generate_random_string()
    print('client_oid: ' + client_oid)

    # Create the prehash string
    prehash_string = f'{timestamp}GET/api/mix/v1/position/allPosition-v2?productType=umcbl'

    # Generate the signature
    signature_base64 = generate_signature(prehash_string)

    # Create the headers
    headers = {
        'ACCESS-KEY': API_KEY,
        'ACCESS-SIGN': signature_base64,
        'ACCESS-TIMESTAMP': str(timestamp),
        'ACCESS-PASSPHRASE': API_PASSPHRASE,
        'Content-Type': 'application/json'
    }

    # Send the POST request
    response = requests.get(url, headers=headers)

    # Print the response
    print(response.status_code)
    print(response.json())
    return response.json()

def get_single_symbol_ticker(symbol):
    # API endpoint for placing orders
    url = 'https://api.coincatch.com/api/mix/v1/market/ticker?symbol=' + symbol

    #Generate client_oid
    client_oid = "unique_client_order_id" + generate_random_string()
    print('client_oid: ' + client_oid)

    # Create the prehash string
    prehash_string = f'{timestamp}GET/api/mix/v1/market/ticker?symbol=' + symbol

    # Generate the signature
    signature_base64 = generate_signature(prehash_string)

    # Create the headers
    headers = {
        'ACCESS-KEY': API_KEY,
        'ACCESS-SIGN': signature_base64,
        'ACCESS-TIMESTAMP': str(timestamp),
        'ACCESS-PASSPHRASE': API_PASSPHRASE,
        'Content-Type': 'application/json'
    }

    # Send the POST request
    response = requests.get(url, headers=headers)

    # Print the response
    print(response.status_code)
    print(response.json())
    return response.json()

def get_single_account():
    # API endpoint for placing orders
    url = 'https://api.coincatch.com/api/mix/v1/account/account?symbol=BTCUSDT_UMCBL&marginCoin=USDT'

    #Generate client_oid
    client_oid = "unique_client_order_id" + generate_random_string()
    print('client_oid: ' + client_oid)

    # Create the prehash string
    prehash_string = f'{timestamp}GET/api/mix/v1/account/account?symbol=BTCUSDT_UMCBL&marginCoin=USDT'

    # Generate the signature
    signature_base64 = generate_signature(prehash_string)

    # Create the headers
    headers = {
        'ACCESS-KEY': API_KEY,
        'ACCESS-SIGN': signature_base64,
        'ACCESS-TIMESTAMP': str(timestamp),
        'ACCESS-PASSPHRASE': API_PASSPHRASE,
        'Content-Type': 'application/json'
    }

    # Send the POST request
    response = requests.get(url, headers=headers)

    # Print the response
    print(response.status_code)
    print(response.json())
    return response.json()
