def check_age(age: int)->bool:
    if (type(age) == type(int()) and 0 <= age <= 30):
        return True
    print("Invalid input")
    return False

def check_name(name: str)->bool:
    if name.isalpha():
        return True
    return False
