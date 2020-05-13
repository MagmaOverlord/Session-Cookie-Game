#add bootstrap
import flask
from flask import request, render_template, make_response, session
from random import choice

app = flask.Flask(__name__)
app.secret_key = "abcdefghijklmnopqrstuvwxyz"

week = 60*60*24*7

@app.route('/', methods = ["GET", "POST"])
def index():
    return flask.render_template('index.html')

@app.route('/game')
def game():
    if 'score' not in session:
        session['score'] = 0
    if request.method == 'POST':
        form = request.form
        resp = make_response(render_template("index.html", score = session["score"]))
        resp.set_cookie('bgcolor', form['bgcolor'], max_age = week)
        resp.set_cookie('gmcolor', form['gmcolor'], max_age = week)
        resp.set_cookie('imsrc', form['imsrc'], max_age = week)
        resp.set_cookie('fncolor', form['fncolor'], max_age = week)
        return resp
    return flask.render_template('game.html', score = session['score'])

@app.route('/settings')
def settings():
    return flask.render_template('settings.html')

@app.route('/score', methods=["POST"])
def score():
    session['score'] += 1
    return str(session['score'])

@app.route('/signup')
def signup():
    return flask.render_template('signup.html')

@app.route('/login')
def login():
    return flask.render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5648)