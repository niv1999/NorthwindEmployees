class CityModel:

    def __init__(self, id, name, country_id):
        self.id = id
        self.name = name
        self.country_id = country_id

    @staticmethod
    def get_city_name(id):
        if not id: return None
        from logic.employee_logic import EmployeesLogic
        logic = EmployeesLogic()
        city_name = logic.get_city_name(id)["name"]
        return city_name
    
    @staticmethod
    def dict_to_model(dictionary):
        city = CityModel(dictionary["id"], dictionary["name"], dictionary["country_id"])
        return city
    
    @staticmethod
    def dicts_to_models(list):
        cities = []
        for item in list:
            city = CityModel.dict_to_model(item)
            cities.append(city)
        return cities