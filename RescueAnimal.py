class RescueAnimal:
    name = ""
    animal_type = ""
    gender = ""
    age = 0
    weight = 0.0
    acquisition_date = ""
    acquisition_country = ""
    training_status = ""
    reserved = False
    in_service_country = ""

    def __init__(self, name, animal_type, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country):
        self.name = name
        self.animal_type = animal_type
        self.gender = gender
        self.age = age
        self.weight = weight
        self.acquisition_date = acquisition_date
        self.acquisition_country = acquisition_country
        self.training_status = training_status
        self.reserved = reserved
        self.in_service_country = in_service_country
    
    def get_name(self):
        return self.name
    
    def get_animal_type(self):
        return self.animal_type
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    def get_weight(self):
        return self.weight
    
    def get_acquisition_date(self):
        return self.acquisition_date
    
    def get_acquisition_country(self):
        return self.acquisition_country
    
    def get_training_status(self):
        return self.training_status
    
    def get_reserved(self):
        return self.reserved
    
    def get_in_service_country(self):
        return self.in_service_country
    

    def set_name(self, name):
        self.name = name
    
    def set_animal_type(self, animal_type):
        self.animal_type = animal_type
    
    def set_gender(self, gender):
        self.gender = gender
    
    def set_age(self, age):
        self.age = age
    
    def set_weight(self, weight):
        self.weight = weight
    
    def set_acquisition_date(self, acquisition_date):
        self.acquisition_date = acquisition_date
    
    def set_acquisition_country(self, acquisition_country):
        self.acquisition_country = acquisition_country
    
    def set_training_status(self, training_status):
        self.training_status = training_status
    
    def set_reserved(self, reserved):
        self.reserved = reserved
    
    def set_in_service_country(self, in_service_country):
        self.in_service_country = in_service_country

    

    