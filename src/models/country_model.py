class CountryModel:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get_country_name(id):
        if not id: return None
        from logic.employee_logic import EmployeesLogic
        logic = EmployeesLogic()
        country_name = logic.get_country_name(id)["name"]
        return country_name
    
    @staticmethod
    def dict_to_model(dictionary):
        country = CountryModel(dictionary["id"], dictionary["name"])
        return country
    
    @staticmethod
    def dicts_to_models(list):
        countries = []
        for item in list:
            country = CountryModel.dict_to_model(item)
            countries.append(country)
        return countries