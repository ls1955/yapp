from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", tuna_endpoint="tuna")

@app.route("/tuna")
def tuna():
    return render_template("tuna.html", home_endpoint="/")

@app.route("/users/new")
def new_user():
    return render_template("user_form.html")

@app.route("/users/create", methods=("POST",))
def create_user():
    return render_template("user_form.html")

@app.route("/about")
def about():
    return "<p>Made with love by Sheng1955</p>"
