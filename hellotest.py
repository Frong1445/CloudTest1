from flask import Flask, render_template
app = Flask(__name__)

@app.route("/John")
def John():
    return "Hello John"

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/Welcome/<name>')
def Welcome_name(name):
    return "Welcome"+name+'!'

@app.route('/aboutUs')
def aboutUs():
    return render_template("aboutUs.html")

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8000)