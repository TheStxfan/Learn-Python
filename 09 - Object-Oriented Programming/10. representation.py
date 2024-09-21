class MotorCycle:
    def __init__(self, name, speed, brand):
        self.name = name
        self.speed = speed
        self.brand = brand

    # Skip to line 12 for now
    # def __repr__(self):
    #     return repr((self.name, self.speed, self.brand))


motorcycles = MotorCycle("Ducati", 335, "Red")

print(motorcycles)  # This will print the objects and their memory addresses. Run the code to check.

# Now uncomment the __repr__ method above to print a readable representation of the objects and run the code again.
