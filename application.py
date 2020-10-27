from flask import Flask
app = Flask(__name__)

import test

@app.route("/")
def hello():
    return test.ret_message()
