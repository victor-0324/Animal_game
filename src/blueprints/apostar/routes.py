from flask import Blueprint, request, render_template, url_for, redirect

apostar_app = Blueprint("apostar_app", __name__, url_prefix="/apostar", template_folder='templates',static_folder='static')


# Tela de apostar

@apostar_app.route("/", methods=["GET", "POST"])
def mostrar():   
    return render_template("pages/apostar/mostrar.html")