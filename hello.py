from flask import Flask
from time import sleep

app = Flask(__name__)


# Decoration Function
# delay_decorator(function):

#   def wrapper_function():
# Do something after
# sleep(2)
# function()
# Do something before
# return wrapper_function
# And you can add it as:
# @delay_decorator

def bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    
    return wrapper


def h1(function):
    def wrapper():
        # msg = function()
        return f'<h1>{function()}</h1>'

    return wrapper


@app.route('/')
@bold
@h1
def hello_word():
    return 'Hello, world'


@app.route('/bye')
def bye():
    return "Bye!"


@app.route('/name')
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
# This is the same as type flask run
