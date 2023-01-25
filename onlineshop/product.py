class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getattr(self):
        return (self.name, self.price)

    @classmethod
    def setobject(cls, name, price):
        return cls(name, price)

def prodObj(name="", price = None):
    prod = Product.setobject(name, price)
    return (prod.name, prod.price)
