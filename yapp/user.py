from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from yapp.db import get_db

bp = Blueprint("user", __name__)

@bp.route("/")
def index():
    db = get_db()
    users = db.execute("SELECT name FROM users")

    return render_template("user/index.html", users=users)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        password_confirmation = request.form["password_confirmation"]

        if password != password_confirmation:
            flash("Password should be equal to password confirmation", "error")
        else:
            # TODO: Encrypt password according to encrypt option
            db = get_db()
            db.execute(
                "INSERT INTO users (name, username, password, encrypted_password)"
                "VALUES (?, ?, ?, ?)",
                (name, username, password, password)
            )
            db.commit()
            return redirect(url_for("index"))
    return render_template("user/create.html")

