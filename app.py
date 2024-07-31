from flask import Flask

# Your API key and secret
API_KEY = 'cc_59c730b0f45a7f8f9d7a43483cf09cb1'
API_SECRET = '73b3ad0e84916ce9103c3582d168e88bf1b7cf99376290d0992904c60ab86d73'
API_PASSPHRASE = '13731373'  # Replace with your actual passphrase

# Generate the current timestamp in milliseconds
timestamp = int(time.time() * 1000)

app = Flask(__name__)

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

@app.route('/')
def home():
    get_single_account()

if __name__ == '__main__':
    app.run(debug=True)
