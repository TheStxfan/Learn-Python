class MotorBike:
    def __init__(self, speed):  # Constructor with 'speed' parameter
        # Skip to line 6 for now
        # self.speed = speed

        print(f"MotorBike instance created with speed {speed}.")


# Creating MotorBike instances
honda = MotorBike(50)
ducati = MotorBike(150)

"""
The speed parameter can be accessed within the constructor when a new object is created, 
but it is not stored as object data. 
As a result, accessing `honda.speed` or `ducati.speed` will cause an error. Try running the code to observe this behavior.
"""

print(f"Honda speed = {honda.speed}")
print(f"Ducati speed = {ducati.speed}")

"""
To store the speed parameter as object data, you can use 'self.speed = speed' in the constructor. 
This will allow you to access the speed attribute using `honda.speed` and `ducati.speed`. 
Uncomment line 4 and run the code again to see the change.
"""
