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

