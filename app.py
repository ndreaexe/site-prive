from flask import Flask

app = Flask(__name__)

@app.route("/monliensecret123")
def secret():
    return "<h1>Bienvenue sur mon site privé 🔐</h1>"

if __name__ == "__main__":
    app.run()