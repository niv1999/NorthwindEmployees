from flask import Flask, render_template
from views.home_view import home_blueprint
from views.employees_view import employees_blueprint
from views.auth_view import auth_blueprint

app = Flask(__name__)

app.secret_key = "Northwind is a cool website"

app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(employees_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error=error)

@app.errorhandler(Exception)
def catch_all(error):
    return render_template("500.html", error=error)
    