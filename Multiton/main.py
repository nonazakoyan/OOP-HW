class Multiton:
    __count = 3
    __instance_list = [None] * __count
    __x = 0
    def __new__(cls, *args, **kwargs):
        index = (cls.__x % cls.__count)
        if cls.__instance_list[index] is None:
            cls.__instance_list[index] = super().__new__(cls)
        cls.__x+=1
        return cls.__instance_list[index]
        

    def __init__(self, check):
        self.check = check


m = Multiton(1)
m1 = Multiton(5)
m2 = Multiton(12)
m3 = Multiton(5)
m4 = Multiton(6)
print(m, m1, m2, m3, m4)