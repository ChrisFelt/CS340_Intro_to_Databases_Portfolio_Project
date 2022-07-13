from flask import Flask, render_template, json, redirect
# from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)


# homepage routes to index
@app.route('/')
def home():
    return redirect("/index")


@app.route('/index')
def index():
    return render_template("index.html")


# user route
@app.route('/user', methods=["POST", "GET"])
def user():
    return render_template("user.html")


# Listener
if __name__ == "__main__":
    # Start the app on port 3000, it will be different once hosted
    app.run(port=17999, debug=True)
