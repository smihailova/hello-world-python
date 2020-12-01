#!/usr/bin/env python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/template')
def hello_template():
    return render_template('index.html')

@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello %s, Sofia and Gideon!' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0')