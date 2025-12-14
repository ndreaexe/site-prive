from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Mon site est en ligne 🚀"
