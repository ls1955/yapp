from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from yapp.db import get_db

bp = Blueprint("user", __name__)

@bp.route("/")
def index():
    return "Goodbye, world."

