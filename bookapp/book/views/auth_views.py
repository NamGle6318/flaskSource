from flask import Blueprint, redirect, url_for, render_template
from book.forms import UserForm

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/signup/", methods=["GET", "HOST"])  # /auth/signup/
def signup():
    form = UserForm()
    return render_template("auth/signup.html")
