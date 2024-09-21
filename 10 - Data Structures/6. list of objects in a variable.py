class MotorCycle:
    def __init__(self, name, speed, brand):
        self.name = name
        self.speed = speed
        self.brand = brand

    def __repr__(self):
        return repr((self.name, self.speed, self.brand))


# Storing a representable list of objects inside a variable
motorcycles = [MotorCycle("Ducati", 335, "Red"),
               MotorCycle("Honda", 1400, "Orange"),
               MotorCycle("Yamaha", 299, "Green")]

print(motorcycles)
