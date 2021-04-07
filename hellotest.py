from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "My name is Suphavit Thepsuriyawet"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
