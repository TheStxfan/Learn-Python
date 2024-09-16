class MotorBike:
    def __init__(self, speed):
        self.speed = speed

    # Modifying the State of the Object within the Class
    def increase_speed(self, amount):
        self.speed += amount

    def decrease_speed(self, amount):
        self.speed -= amount


# Creating MotorBike instances
honda = MotorBike(50)    # Total speed: 50
ducati = MotorBike(150)  # Total speed: 150

print(f"Honda speed = {honda.speed}")
print(f"Ducati speed = {ducati.speed}")
print()

# Modifying the State of the Object outside the Class
honda.speed += 100   # Total speed: 150
ducati.speed += 150  # Total speed: 300

print(f"Honda speed = {honda.speed}")
print(f"Ducati speed = {ducati.speed}")
print()

# Calling 'increase_speed()' Method for the specified Object
honda.increase_speed(50)  # Total speed: 200

print(f"Honda speed = {honda.speed}")
print(f"Ducati speed = {ducati.speed}")
print()

# Calling 'increase_speed()' Method for the specified Objects
honda.decrease_speed(25)    # Total speed: 175
ducati.decrease_speed(25)  # Total speed: 275

print(f"Honda speed = {honda.speed}")
print(f"Ducati speed = {ducati.speed}")
print()


