from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'سلام! این یک پروژه فلاسک ساده است.'

if __name__ == '__main__':
    app.run(debug=True)
