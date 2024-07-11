from flask import Blueprint, render_template, send_file, request, url_for, redirect
from facades.employee_facade import EmployeeFacade
from facades.auth_facade import AuthFacade
from utils.image_handler import ImageHandler
import json
from models.client_errors import ResourceNotFound, ValidationError, AuthError

employees_blueprint = Blueprint("employees_view", __name__)

employee_facade = EmployeeFacade()
auth_facade = AuthFacade()

@employees_blueprint.route("/employees")
def employees_list():
    all_employees = employee_facade.get_all_employees()
    return render_template("all_employees.html", employees = all_employees, active = "our_employees")

@employees_blueprint.route("/employees/<int:id>")
def one_employee(id):
    try:
        next_id = employee_facade.get_next_employee_id(id)
        previous_id = employee_facade.get_previous_employee_id(id)
        one_employee = employee_facade.get_one_employee(id)
        return render_template("employee.html", employee = one_employee, next_id = next_id, previous_id = previous_id)
    except ResourceNotFound as err:
        return render_template("404.html", error = err.message)

@employees_blueprint.route("/employees/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)

@employees_blueprint.route("/employees/add", methods=['GET', 'POST'])
def insert():
    try:
        auth_facade.block_anonymous()
        if request.method == "GET":
            all_countries = employee_facade.get_all_countries() 
            all_cities = employee_facade.get_all_cities()
            cities_json = json.dumps([city.__dict__ for city in all_cities])
            return render_template('add_employee.html', countries = all_countries, cities_json = cities_json, active = "add_employee")
        employee_facade.add_employee()
        return redirect(url_for('employees_view.employees_list'))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    except ValidationError as err:
        all_countries = employee_facade.get_all_countries() 
        all_cities = employee_facade.get_all_cities()
        cities_json = json.dumps([city.__dict__ for city in all_cities])
        return render_template("add_employee.html", countries = all_countries, cities_json = cities_json, error=err.message, active = "add_employee")

@employees_blueprint.route("/employees/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    try:
        auth_facade.block_anonymous()
        if request.method == "GET":
            employee = employee_facade.get_one_employee(id)
            all_countries = employee_facade.get_all_countries() 
            all_cities = employee_facade.get_all_cities()
            cities_json = json.dumps([city.__dict__ for city in all_cities])
            return render_template("edit_employee.html", employee = employee, countries = all_countries, cities_json = cities_json)
        employee_facade.update_employee()
        return redirect(url_for("employees_view.one_employee", id=id))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    except ValidationError as err:
        all_countries = employee_facade.get_all_countries() 
        all_cities = employee_facade.get_all_cities()
        cities_json = json.dumps([city.__dict__ for city in all_cities])
        return render_template("edit_employee.html", error = err.message, employee = err.model, countries = all_countries, cities_json = cities_json)

@employees_blueprint.route("/employees/delete/<int:id>")
def delete(id):
    try:
        auth_facade.block_anonymous()
        auth_facade.block_non_admin()   
        employee_facade.delete_employee(id)
        return redirect(url_for("employees_view.employees_list"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))