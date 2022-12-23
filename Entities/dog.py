import checker as ch

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
        if ch.check_name(name):
            self.name = name
    def set_age(self, age):
        if ch.check_age(age):
            self.age = age

