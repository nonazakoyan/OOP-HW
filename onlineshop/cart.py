import product

class ShoppingCart():
    def __init__(self):
        self.prod = []
        self.ProdInfo = {}


    def prod_count(self):
        keyslist = []
        for i in self.prod:
            keyslist.append(i[0])
        for i in keyslist:
            self.ProdInfo[f'{i}'] = keyslist.count(i)

    def add_prod(self, prod_name, prod_price):
        self.prod.append(product.prodObj(prod_name, prod_price))
        self.prod_count()

    def getattr(self):
        return (self.prod, self.ProdInfo)

    def take_prod(self, prod_name):
        if self.ProdInfo.get(prod_name) == None:
            print("Product is not found.")
        elif self.ProdInfo[prod_name] == 0:
            print("Procuct is out of stock")
        else:
            self.ProdInfo[prod_name] -= 1
        print (self.ProdInfo)

warehause = ShoppingCart()
warehause.add_prod("phone", 120)
warehause.add_prod("phone", 120)
warehause.add_prod("phone", 120)
warehause.add_prod("phone", 120)
warehause.add_prod("sjdk", 15)
warehause.add_prod("sjdk", 15)
warehause.add_prod("sjdk", 15)
warehause.add_prod("sjdk", 15)
warehause.add_prod("sjdk", 15)
# print(warehause.getattr())






