class LandAnimal:
    def __init__(self):
        super().__init__()  # Calls the superclasses constructor to initialize attributes and methods in the subclass.
        self.walking_speed = 5

    def increase_walking_speed(self, amount):
        self.walking_speed += amount


class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.swimming_speed = 10

    def increase_swimming_speed(self, amount):
        self.swimming_speed += amount


class Amphibian(WaterAnimal, LandAnimal):
    def __init__(self):
        super().__init__()


amphibian = Amphibian()

print(amphibian.walking_speed)
print(amphibian.swimming_speed)

amphibian.increase_walking_speed(25)
amphibian.increase_swimming_speed(50)

print()
print(amphibian.walking_speed)
print(amphibian.swimming_speed)






















