from utils.dal import DAL
from models.employee_model import EmployeeModel
from models.country_model import CountryModel
from models.city_model import CityModel
from utils.image_handler import ImageHandler

class EmployeesLogic:

    def __init__(self):
        self.dal = DAL()

    def get_all_employees(self):
        sql = "SELECT * FROM employees"
        employees_list =  self.dal.get_table(sql)
        return EmployeeModel.dicts_to_models(employees_list)
    
    def get_one_employee(self, id):
        sql = "SELECT * FROM employees WHERE id=%s"
        employee_dict = self.dal.get_scalar(sql, (id, ))
        if not employee_dict: return None
        return EmployeeModel.dict_to_model(employee_dict)
    
    def add_employee(self, employee):
        employee_img = ImageHandler.save_image(employee.image)
        sql = '''INSERT INTO employees (first_name, last_name, title, title_of_courtesy, birth_date, hire_date, country_id, city_id, address, postal_code, phone, notes, image_name) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        params = (employee.first_name, 
                  employee.last_name,
                  employee.title,
                  employee.title_of_courtesy,
                  employee.birth_date,
                  employee.hire_date,
                  employee.country_id,
                  employee.city_id,
                  employee.address,
                  employee.postal_code,
                  employee.phone,
                  employee.notes,
                  employee_img)
        self.dal.insert(sql, params)

    def update_employee(self, employee):
        old_image_name = self.__get_old_image_name(employee.id)
        image_name = ImageHandler.update_image(old_image_name, employee.image)
        sql = "UPDATE employees SET first_name=%s, last_name=%s, title=%s, title_of_courtesy=%s, birth_date=%s, hire_date=%s, country_id=%s, city_id=%s, address=%s, postal_code=%s, phone=%s, notes=%s, image_name=%s WHERE id=%s"
        params = (employee.first_name, 
                  employee.last_name,
                  employee.title,
                  employee.title_of_courtesy,
                  employee.birth_date,
                  employee.hire_date,
                  employee.country_id,
                  employee.city_id,
                  employee.address,
                  employee.postal_code,
                  employee.phone,
                  employee.notes,
                  image_name,
                  employee.id)
        self.dal.update(sql, params)

    def delete_employee(self, id):
        image_name = self.__get_old_image_name(id)
        ImageHandler.delete_image(image_name)
        sql = "DELETE FROM employees WHERE id=%s"
        self.dal.delete(sql, (id, ))

# ----------------------------------------------------------------------
# Utilities: 
                
    def __get_old_image_name(self, id):
        sql = "SELECT image_name FROM employees WHERE id=%s"
        old_image_name = self.dal.get_scalar(sql, (id, ))["image_name"]
        return old_image_name

    def get_next_employee_id(self, id):
        sql = "SELECT MIN(id) AS id FROM employees WHERE id > %s"
        return self.dal.get_scalar(sql, (id, ))["id"]
    
    def get_previous_employee_id(self, id):
        sql = "SELECT MAX(id) AS id FROM employees WHERE id < %s"
        return self.dal.get_scalar(sql, (id, ))["id"]

# ----------------------------------------------------------------------
# Countries & Cities:
    
    def get_country_name(self, country_id):
        sql = "SELECT name FROM countries WHERE id=%s"
        return self.dal.get_scalar(sql, (country_id, ))
    
    def get_all_countries(self):
        sql = "SELECT * FROM countries"
        countries_list = self.dal.get_table(sql)
        return CountryModel.dicts_to_models(countries_list)
    
    def get_city_name(self, city_id):
        sql = "SELECT name FROM cities WHERE id=%s"
        return self.dal.get_scalar(sql, (city_id, ))
    
    def get_all_cities(self):
        sql = "SELECT * FROM cities"
        cities_list =  self.dal.get_table(sql)
        return CityModel.dicts_to_models(cities_list)
