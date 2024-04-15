import os
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24).hex()

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
    username = request.form["username"]
    password = request.form["password"]
    password_c = request.form["password_confirm"]

    if password != password_c:
        flash("The passwords must match.", "error")
        return render_template("user_form.html", request=request)
    flash("Successful created user.", "info")
    return render_template("user_form.html")

@app.route("/about")
def about():
    return "<p>Made with love by Sheng1955</p>"
