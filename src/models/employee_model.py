from datetime import datetime
from .city_model import CityModel
from .country_model import CountryModel


class EmployeeModel:

    def __init__(self, id, first_name, last_name, title, title_of_courtesy, birth_date, hire_date, country_id, city_id, address, postal_code, phone, notes, image):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.title_of_courtesy = title_of_courtesy
        self.birth_date = birth_date
        self.hire_date = hire_date
        self.country_id = country_id
        self.city_id = city_id
        self.address = address
        self.postal_code = postal_code
        self.phone = phone
        self.notes = notes
        self.image = image
        self.country_name = CountryModel.get_country_name(country_id)
        self.city_name = CityModel.get_city_name(city_id)
    
    def validate_insert(self):
        if not self.first_name: return "Missing First Name"
        if not self.last_name: return "Missing Last Name"
        if not self.title: return "Missing Title"
        if not self.title_of_courtesy: return "Missing Title of Courtesy"
        if not self.birth_date: return "Missing Birth Date"
        if not self.hire_date: return "Missing Hire Date"
        if not self.country_id: return "Missing Country ID"
        if not self.city_id: return "Missing City ID"
        if not self.address: return "Missing Address"
        if not self.postal_code: return "Missing Postal Code"
        if not self.phone: return "Missing Phone"
        if not self.notes: return "Missing Notes"
        if not self.image: return "Missing Image"
        if len(self.first_name) < 2 or len(self.first_name) > 40: return "First name must be 2-40 characters"
        if len(self.last_name) < 2 or len(self.last_name) > 100: return "Last name must be 2-100 characters"
        if len(self.title) < 2 or len(self.title) > 150: return "Title must be 2-150 characters"
        if len(self.title_of_courtesy) < 3 or len(self.title) > 100: return "Title must be 3-100 characters"
        current_time = datetime.now()
        birth_date_object = datetime.strptime(self.birth_date, "%Y-%m-%d")
        hire_date_object = datetime.strptime(self.hire_date, "%Y-%m-%d")
        if birth_date_object > current_time: return "Birth Date can't be in the future"
        if hire_date_object > current_time: return "Hire Date can't be in the future"
        if birth_date_object > hire_date_object: return "Hire Date can't be before the birth date"
        if current_time.year - birth_date_object.year < 18 or hire_date_object.year - birth_date_object.year < 18: return "Can't hire under-age people!"
        if not self.country_name: return "The country does not exist in the database."
        if not self.city_name: return "The city does not exist in the database."
        if len(self.address) < 5 or len(self.address) > 200: return "Address must be 5-200 characters"
        if len(self.postal_code) < 2 or len(self.postal_code) > 20: return "Postal code must be 2-20 characters"
        if len(self.phone) < 7 or len(self.phone) > 20: return "Phone must be 7-20 characters"
        if len(self.notes) < 5 or len(self.notes) > 1000: return "Notes must be 5-1000 characters"
        return None
        
    def validate_update(self):
        if not self.id: return "Missing ID"
        if not self.first_name: return "Missing First Name"
        if not self.last_name: return "Missing Last Name"
        if not self.title: return "Missing Title"
        if not self.title_of_courtesy: return "Missing Title of Courtesy"
        if not self.birth_date: return "Missing Birth Date"
        if not self.hire_date: return "Missing Hire Date"
        if not self.country_id: return "Missing Country ID"
        if not self.city_id: return "Missing City ID"
        if not self.address: return "Missing Address"
        if not self.postal_code: return "Missing Postal Code"
        if not self.phone: return "Missing Phone"
        if not self.notes: return "Missing Notes"
        if len(self.first_name) < 2 or len(self.first_name) > 40: return "First name must be 2-40 characters"
        if len(self.last_name) < 2 or len(self.last_name) > 100: return "Last name must be 2-100 characters"
        if len(self.title) < 2 or len(self.title) > 150: return "Title must be 2-150 characters"
        if len(self.title_of_courtesy) < 3 or len(self.title) > 100: return "Title must be 3-100 characters"
        current_time = datetime.now()
        birth_date_object = datetime.strptime(self.birth_date, "%Y-%m-%d")
        hire_date_object = datetime.strptime(self.hire_date, "%Y-%m-%d")
        if birth_date_object > current_time: return "Birth Date can't be in the future"
        if hire_date_object > current_time: return "Hire Date can't be in the future"
        if birth_date_object > hire_date_object: return "Hire Date can't be before the birth date"
        if current_time.year - birth_date_object.year < 18 or hire_date_object.year - birth_date_object.year < 18: return "Can't hire under-age people!"
        if not self.country_name: return "The country does not exist in the database."
        if not self.city_name: return "The city does not exist in the database."
        if len(self.address) < 5 or len(self.address) > 200: return "Address must be 5-200 characters"
        if len(self.postal_code) < 2 or len(self.postal_code) > 20: return "Postal code must be 2-20 characters"
        if len(self.phone) < 7 or len(self.phone) > 20: return "Phone must be 7-20 characters"
        if len(self.notes) < 5 or len(self.notes) > 1000: return "Notes must be 5-1000 characters"
        return None


    @staticmethod
    def dict_to_model(dictionary):
        employee = EmployeeModel(
            dictionary["id"],
            dictionary["first_name"],
            dictionary["last_name"],
            dictionary["title"],
            dictionary["title_of_courtesy"],
            dictionary["birth_date"],
            dictionary["hire_date"],
            dictionary["country_id"],
            dictionary["city_id"],
            dictionary["address"],
            dictionary["postal_code"],
            dictionary["phone"],
            dictionary["notes"],
            dictionary["image_name"]
        )
        return employee
    
    @staticmethod
    def dicts_to_models(list):
        employees = []
        for item in list:
            employee = EmployeeModel.dict_to_model(item)
            employees.append(employee)
        return employees