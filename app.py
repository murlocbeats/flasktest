from flask import Flask
from trader import *

app = Flask(__name__)

@app.route('/')
def home():
    get_single_account()

if __name__ == '__main__':
    app.run(debug=True)
