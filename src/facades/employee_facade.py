from logic.employee_logic import EmployeesLogic
from flask import request
from models.employee_model import EmployeeModel
from models.client_errors import ResourceNotFound, ValidationError

class EmployeeFacade:

    def __init__(self):
        self.logic = EmployeesLogic()

    def get_all_employees(self):
        return self.logic.get_all_employees()
    
    def get_one_employee(self, employee_id):
        employee = self.logic.get_one_employee(employee_id)
        if not employee: raise ResourceNotFound(employee_id)
        return employee
    
    def get_all_countries(self):
        return self.logic.get_all_countries()
    
    def get_all_cities(self):
        return self.logic.get_all_cities()
    
    def get_next_employee_id(self, id):
        return self.logic.get_next_employee_id(id)

    def get_previous_employee_id(self, id):
        return self.logic.get_previous_employee_id(id)
    
    def add_employee(self):
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        title = request.form.get("title")
        title_of_courtesy = request.form.get("title_of_courtesy")
        birth_date = request.form.get("birth_date")
        hire_date = request.form.get("hire_date")
        country_id = request.form.get("country_id")
        city_id = request.form.get("city_id")
        address = request.form.get("address")
        postal_code = request.form.get("postal_code")
        phone = request.form.get("phone")
        notes = request.form.get("notes")
        image_name = request.files["image"]
        employee = EmployeeModel(None, first_name, last_name, title, title_of_courtesy, birth_date, hire_date, country_id, city_id, address, postal_code, phone, notes, image_name)
        error = employee.validate_insert()
        if error: raise ValidationError(error, employee)
        self.logic.add_employee(employee)

    def update_employee(self):
        id = request.form.get("id")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        title = request.form.get("title")
        title_of_courtesy = request.form.get("title_of_courtesy")
        birth_date = request.form.get("birth_date")
        hire_date = request.form.get("hire_date")
        country_id = request.form.get("country_id")
        city_id = request.form.get("city_id")
        address = request.form.get("address")
        postal_code = request.form.get("postal_code")
        phone = request.form.get("phone")
        notes = request.form.get("notes")
        image_name = request.files["image"]
        employee = EmployeeModel(id, first_name, last_name, title, title_of_courtesy, birth_date, hire_date, country_id, city_id, address, postal_code, phone, notes, image_name)
        error = employee.validate_update()
        if error: raise ValidationError(error, employee)
        self.logic.update_employee(employee)

    def delete_employee(self, id):
        self.logic.delete_employee(id)