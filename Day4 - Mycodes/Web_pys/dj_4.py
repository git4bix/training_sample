from flask import Flask, url_for, redirect, abort, request
app = Flask(__name__)

@app.route("/")
def index():
    return f'''
    <a href="{url_for('login')}">Login Page</a><br>
    <a href="{url_for('profile', username='elo')}">Ace</a>
'''

@app.route("/login/")
def login():
    abort(420)

#@app.route("/profile/<username>")
#def profile(username):
 #   return f"My name is {username}"

@app.route("/user/<username>")
def profile(username):
    if username != "admin":
        return redirect(url_for('login'))
    else:
        return "Welcome Admin"


app.run()