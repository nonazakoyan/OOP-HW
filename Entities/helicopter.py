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

