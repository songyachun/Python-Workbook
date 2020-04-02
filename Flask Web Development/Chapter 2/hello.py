from flask import make_response
from flask import request
from flask import Flask
app = Flask(__name__)

from flask import redirect
from flask import abort
@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    # user_agent = request.headers.get('User-Agent')
    # return '<p> Your browser is {}</p>'.format(user_agent)
    # return '<h1>Bad Request<h1/>',400
    # response = make_response('<h1>This document carries a cookie</h1>')
    # response.set_cookie('answer', '42')
    # return response
    return redirect('http://www.example.com')



@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,{}!</h1>'.format(name)


if __name__ == "__main__":
    app.run(debug=True)
