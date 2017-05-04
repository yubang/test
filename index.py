# coding:UTF-8

from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return sys.version

@app.route("/debug")
def debug():
    return "debug"

if __name__ == "__main__":
    app.run(port=80)
