#!/usr/bin/python3
"""hello-world-flask"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """----"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """text display"""
    return ('C ' + text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def fun_python(text='is cool'):
    """text display Python"""
    return ('Python ' + text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def fun_number(n):
    """display “n is a number” only if n is an integer"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def fun_template(n):
    """template"""
    return render_template("5-number.html", n=n)

if __name__ == '__main__':
    """main"""
    app.run(host='0.0.0.0', port=5000)
    app.run()
