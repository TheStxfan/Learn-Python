class MotorBike:
    """
    The __init__() method is a constructor in Python classes that initializes a newly created object's attributes.
    'self' refers to the current instance of a class and is used to access its attributes and methods.
    Details on `self` are explained further.
    """
    def __init__(self):
        print("MotorBike instance created.")


# Creating instances of MotorBike
print("\nCreating instances of MotorBike")
honda = MotorBike()  # MotorBike instance created.
ducati = MotorBike()  # MotorBike instance created.

# Adding attributes to the instances
print("\nAdding attributes to the instances")
honda.speed = 50
ducati.speed = 250

# Printing object references (default behavior)
print("\nPrinting object references")
#                      ObjectType - located at - Memory address:
print(honda)   # <__main__.MotorBike object at 0x000002740D430230>
print(ducati)  # <__main__.MotorBike object at 0x000002740D430260>

# Printing the speed attribute of each instance
print("\nPrinting the speed attribute of each instance")
print(honda.speed)   # 50
print(ducati.speed)  # 250

# Modifying and printing the speed attribute of the honda instance
print("\nModifying and printing the speed attribute of the honda instance")
honda.speed = 150
print(honda.speed)   # 150
print(ducati.speed)  # 250