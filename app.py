from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", tuna_endpoint="tuna")

@app.route("/tuna")
def tuna():
    return render_template("tuna.html", home_endpoint="/")
