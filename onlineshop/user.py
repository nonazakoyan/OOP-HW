import cart

class User():
    def __init__(self, email, id):
        self.email = email
        self.id = id

    @classmethod
    def setobject(cls, name, id):
        return cls(name, id)

    def by(self, prod_name):
        cart.warehause.take_prod(prod_name)

user = User.setobject("name", "id")
user.by("phone")
user.by("phone")
user.by("phone")
user.by("5")
