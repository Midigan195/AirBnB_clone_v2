#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """print web"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Print Web """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """print C follewd by specified text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """
    Print Python followed by specified text variable;
    else text = "is cool"
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """
    If variable is a number print;
    is a number
    """
    return '{:d} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Display html page if variable is a number.
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    Display html page if variable is even or odd
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
