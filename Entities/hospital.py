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
