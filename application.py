from flask import Flask
app = Flask(__name__)

import test

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/test")
def hello_test():
    return test.ret_message()