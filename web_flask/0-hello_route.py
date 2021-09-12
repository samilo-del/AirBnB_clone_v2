#!/usr/bin/python3
"""hello-world-flask"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """----"""
    return "Hello HBNB!"

if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
