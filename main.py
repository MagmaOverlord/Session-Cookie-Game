import flask
from flask import request, render_template, make_response, session
from random import choice

app = flask.Flask(__name__)
app.secret_key = "abcdefghijklmnopqrstuvwxyz"

@app.route('/')
def index():
	return flask.render_template('index.html')

@app.route('/settings')
def settings():
    return flask.render_template('settings.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5648)