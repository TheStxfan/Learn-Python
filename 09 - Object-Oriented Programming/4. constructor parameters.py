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
As a result, accessing `honda.speed` or `ducati.speed` will cause an error. 
Try running the code to observe this behavior.
"""

print(f"Honda speed = {honda.speed}")
print(f"Ducati speed = {ducati.speed}")

"""
To store the speed parameter as object data, you can use 'self.speed = speed' in the constructor. 
This will allow you to access the speed attribute using `honda.speed` and `ducati.speed`. 
Uncomment line 4 and run the code again to see the change.
"""

input("\nPress Enter to continue with the next example.\n")

# Now let's do the same for the empty Book class created in {section 09, file 2}


class Book:
    def __init__(self, title):
        self.title = title


The_12th_Planet = Book("The 12th Planet")
Dandelion_Wine = Book("Dandelion Wine")
The_Martian_Chronicles = Book("The Martian Chronicles")

print(The_12th_Planet.title)
print(Dandelion_Wine.title)
print(The_Martian_Chronicles.title)
