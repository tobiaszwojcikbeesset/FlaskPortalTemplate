from flask import Blueprint, render_template, redirect, make_response

main_bp = Blueprint("main",__name__, template_folder="templates", static_folder="static")

@main_bp.route("/")
def index():
    return "Hallo Word! "

@main_bp.route("/home")
def home_page():
    return render_template("home.html")


@main_bp.route("/profil")
def profil():
    return render_template("home.html")