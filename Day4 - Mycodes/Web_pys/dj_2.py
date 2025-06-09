from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "welcome to my page"

@app.route("/home/<name>")
@app.route("/index/<name>")
def profile(name):
    return f"welcome to my page {name}"

@app.route("/profile/<topic>")
def dynamic_profile(topic):
    return f"Profile {topic} Page"

app.run()