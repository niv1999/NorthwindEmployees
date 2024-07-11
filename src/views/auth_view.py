from flask import Blueprint, render_template, redirect, url_for, request
from facades.auth_facade import AuthFacade
from models.client_errors import ValidationError, AuthError

auth_blueprint = Blueprint("auth_view", __name__)

facade = AuthFacade()

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET": return render_template("register.html", user = {})
        facade.register()
        return redirect(url_for("home_view.home"))
    except ValidationError as err:
        return render_template("register.html", error = err, user = err.model)
    
@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "GET":
            err = request.args.get("error")
            return render_template("login.html", error = err, credentials = {})
        facade.login()
        return redirect(url_for("home_view.home"))
    except (ValidationError, AuthError) as err:
        return render_template("login.html", error = err.message, credentials = err.model)
    
@auth_blueprint.route("/logout")
def logout():
    facade.logout()
    return redirect(url_for("home_view.home"))
