from operator import attrgetter


class MotorCycle:
    def __init__(self, name, speed, brand):
        self.name = name
        self.speed = speed
        self.brand = brand

    def __repr__(self):
        return repr((self.name, self.speed, self.brand))


motorcycles = [MotorCycle("Ducati", 335, "Red"),
               MotorCycle("Honda", 250, "Orange"),
               MotorCycle("Yamaha", 200, "Green")]

print(motorcycles)
motorcycles.sort(key=attrgetter("speed"))  # Sorts based on a specific attribute of objects
print(motorcycles)

motorcycles.sort(key=attrgetter("speed"), reverse=True)
print(motorcycles)

print(max(motorcycles, key=attrgetter("speed")))
print(min(motorcycles, key=attrgetter("speed")))
