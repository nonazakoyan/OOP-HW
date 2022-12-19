class Dog:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def sound(self):
        print("bark")
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_type(self):
        return self.type
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    
class Helicopter:
    def __init__(self, name, uses, manufacturer,
                        max_speed, max_height):
        self.name = name
        self.uses = uses
        self.manufacturer = manufacturer
        self.speed = max_speed
        self.height = max_height

        def get_name(self):
            return self.name
        def get_uses(self):
            return self.uses
        def get_manufacturer(self):
            return self.manufacturer
        def get_speed (self):
            return self.speed 
        def get_height(self):
            return self.height                     

class Hospital:
    list_patients = []
    def __init__(self, name, location, data):
        self.name = name
        self.location = location
        self.data = data

    def add_patient(self, person_name):
        self.list_patients.append(person_name)
    def discharge(self, persone_name):
        self.list_patients.remove(persone_name)
    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def get_data(self):
        return self.data
    def get_list_patients(self):
        return self.list_patients
